#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

import datetime
import glob
import os
import re
import sys
from io import StringIO

from point_spectra_gui import __version__

if sys.version_info < (3, 5):
    sys.exit("ERROR: You need Python 3.5 or higher to use point_spectra_gui.")

args = {}

try:
    from py2app.build_app import py2app

    do_py2app = True
except ImportError:
    do_py2app = False

# this must be imported *after* py2app, because py2app imports setuptools
# which "patches" (read: screws up) the Extension class
from distutils import log
from distutils.command.build import build
from distutils.command.install import install as install
from distutils.dep_util import newer
from distutils.dist import Distribution
from distutils.spawn import find_executable
from setuptools import setup, Command

PACKAGE_NAME = "Point Spectra GUI"


exclude_modules = [
    'ssl', 'bz2',
    'distutils', 'unittest',
    'bdb', 'calendar', 'difflib', 'doctest', 'dummy_thread', 'gzip',
    'optparse', 'pdb', 'plistlib', 'pyexpat', 'quopri', 'repr',
    'stringio', 'tarfile', 'uu'
]

tx_executable = find_executable('tx')


class point_spectra_gui_test(Command):
    description = "run automated tests"
    user_options = [
        ("tests=", None, "list of tests to run (default all)"),
        ("verbosity=", "v", "verbosity"),
    ]

    def initialize_options(self):
        self.tests = []
        self.verbosity = 1

    def finalize_options(self):
        if self.tests:
            self.tests = self.tests.split(",")
        # In case the verbosity flag is used, verbosity is None
        if not self.verbosity:
            self.verbosity = 2
        # Convert to appropriate verbosity if passed by --verbosity option
        self.verbosity = int(self.verbosity)

    def run(self):
        import unittest

        names = []
        for filename in glob.glob("test/test_*.py"):
            name = os.path.splitext(os.path.basename(filename))[0]
            if not self.tests or name in self.tests:
                names.append("test." + name)

        tests = unittest.defaultTestLoader.loadTestsFromNames(names)
        t = unittest.TextTestRunner(verbosity=self.verbosity)
        testresult = t.run(tests)
        if not testresult.wasSuccessful():
            sys.exit("At least one test failed.")


Distribution.locales = None


class point_spectra_gui_install(install):
    user_options = install.user_options + [
        ('install-locales=', None,
         "installation directory for locales"),
        ('localedir=', None, ''),
        ('disable-autoupdate', None, ''),
        ('disable-locales', None, ''),
    ]

    sub_commands = install.sub_commands

    def initialize_options(self):
        install.initialize_options(self)
        self.localedir = None
        self.disable_autoupdate = None
        self.disable_locales = None

    def finalize_options(self):
        install.finalize_options(self)
        # can't use set_undefined_options :/
        self.distribution.get_command_obj('build').localedir = self.localedir
        self.distribution.get_command_obj('build').disable_autoupdate = self.disable_autoupdate
        if self.root is not None:
            self.change_roots('locales')

    def run(self):
        install.run(self)


class point_spectra_gui_build(build):
    user_options = build.user_options + [
        ('build-locales=', 'd', "build directory for locale files"),
        ('localedir=', None, ''),
        ('disable-autoupdate', None, ''),
        ('disable-locales', None, ''),
    ]

    sub_commands = build.sub_commands

    def initialize_options(self):
        build.initialize_options(self)
        self.localedir = None
        self.disable_autoupdate = None
        self.disable_locales = None

    def finalize_options(self):
        build.finalize_options(self)
        if self.localedir is None:
            self.localedir = '/usr/share/locale'
        if self.disable_autoupdate is None:
            self.disable_autoupdate = False

    def run(self):
        build.run(self)


def py_from_ui(uifile):
    return "%s.py" % os.path.splitext(os.path.basename(uifile))[0]


def py_from_ui_with_defaultdir(uifile):
    return os.path.join("point_spectra_gui", "ui", py_from_ui(uifile))


def ui_files():
    for uifile in glob.glob("ui/*.ui"):
        yield (uifile, py_from_ui_with_defaultdir(uifile))


class point_spectra_gui_build_ui(Command):
    description = "build Qt UI files and resources"
    user_options = [
        ("files=", None, "comma-separated list of files to rebuild"),
    ]

    def initialize_options(self):
        self.files = []

    def finalize_options(self):
        if self.files:
            files = []
            for f in self.files.split(","):
                head, tail = os.path.split(f)
                m = re.match(r'(?:ui_)?([^.]+)', tail)
                if m:
                    name = m.group(1)
                else:
                    log.warn('ignoring %r (cannot extract base name)' % f)
                    continue
                uiname = name + '.ui'
                uifile = os.path.join(head, uiname)
                if os.path.isfile(uifile):
                    pyfile = os.path.join(os.path.dirname(uifile),
                                          py_from_ui(uifile))
                    files.append((uifile, pyfile))
                else:
                    uifile = os.path.join('ui', uiname)
                    if os.path.isfile(uifile):
                        files.append((uifile,
                                      py_from_ui_with_defaultdir(uifile)))
                    else:
                        log.warn('ignoring %r' % f)
            self.files = files

    def run(self):
        from PyQt5 import uic
        _translate_re = (
            re.compile(
                r'QtGui\.QApplication.translate\(.*?, (.*?), None, '
                r'QtGui\.QApplication\.UnicodeUTF8\)'),
            re.compile(
                r'\b_translate\(.*?, (.*?)(?:, None)?\)')
        )

        def compile_ui(uifile, pyfile):
            log.info("compiling %s -> %s", uifile, pyfile)
            tmp = StringIO()
            uic.compileUi(uifile, tmp, True)
            source = tmp.getvalue()
            rc = re.compile(r'\n\n#.*?(?=\n\n)', re.MULTILINE | re.DOTALL)
            comment = ("\n\n# Automatically generated - don't edit.\n"
                       "# Use `python setup.py %s` to update it."
                       % _get_option_name(self))
            for r in list(_translate_re):
                source = r.sub(r'(\1)', source)
                source = rc.sub(comment, source)
            f = open(pyfile, "w")
            f.write(source)
            f.close()

        if self.files:
            for uifile, pyfile in self.files:
                compile_ui(uifile, pyfile)
        else:
            for uifile, pyfile in ui_files():
                if newer(uifile, pyfile):
                    compile_ui(uifile, pyfile)


class point_spectra_gui_clean_ui(Command):
    description = "clean up compiled Qt UI files and resources"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for uifile, pyfile in ui_files():
            try:
                os.unlink(pyfile)
                log.info("removing %s", pyfile)
            except OSError:
                log.warn("'%s' does not exist -- can't clean it", pyfile)
        pyfile = os.path.join("point_spectra_gui", "resources.py")
        try:
            os.unlink(pyfile)
            log.info("removing %s", pyfile)
        except OSError:
            log.warn("'%s' does not exist -- can't clean it", pyfile)



_regen_pot_description = "Regenerate po/point_spectra_gui.pot, parsing source tree for new or updated strings"
try:
    from babel import __version__ as babel_version
    from babel.messages import frontend as babel


    def versiontuple(v):
        return tuple(map(int, (v.split("."))))


    # input_dirs are incorrectly handled in babel versions < 1.0
    # http://babel.edgewall.org/ticket/232
    input_dirs_workaround = versiontuple(babel_version) < (1, 0, 0)


    class point_spectra_gui_regen_pot_file(babel.extract_messages):
        description = _regen_pot_description

        def initialize_options(self):
            # cannot use super() with old-style parent class
            babel.extract_messages.initialize_options(self)
            self.output_file = 'po/point_spectra_gui.pot'
            self.input_dirs = 'point_spectra_gui'
            if self.input_dirs and input_dirs_workaround:
                self._input_dirs = self.input_dirs

        def finalize_options(self):
            babel.extract_messages.finalize_options(self)
            if input_dirs_workaround and self._input_dirs:
                self.input_dirs = re.split(r',\s*', self._input_dirs)

except ImportError:
    class point_spectra_gui_regen_pot_file(Command):
        description = _regen_pot_description
        user_options = []

        def initialize_options(self):
            pass

        def finalize_options(self):
            pass

        def run(self):
            sys.exit("Babel is required to use this command (see po/README.md)")


def _get_option_name(obj):
    """Returns the name of the option for specified Command object"""
    for name, klass in obj.distribution.cmdclass.items():
        if obj.__class__ == klass:
            return name
    raise Exception("No such command class")


class point_spectra_gui_patch_version(Command):
    description = "Update point_spectra_gui_BUILD_VERSION_STR for daily builds"
    user_options = [
        ('platform=', 'p', "platform for the build version, ie. osx or win"),
    ]

    def initialize_options(self):
        self.platform = sys.platform

    def finalize_options(self):
        pass

    def run(self):
        self.patch_version('point_spectra_gui/__init__.py')

    def patch_version(self, filename):
        regex = re.compile(r'^point_spectra_gui_BUILD_VERSION_STR\s*=.*$', re.MULTILINE)
        with open(filename, 'r+b') as f:
            source = (f.read()).decode()
            build = self.platform + '_' + datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
            patched_source = regex.sub('point_spectra_gui_BUILD_VERSION_STR = "%s"' % build, source).encode()
            f.seek(0)
            f.write(patched_source)
            f.truncate()


def cflags_to_include_dirs(cflags):
    cflags = cflags.split()
    include_dirs = []
    for cflag in cflags:
        if cflag.startswith('-I'):
            include_dirs.append(cflag[2:])
    return include_dirs


def _point_spectra_gui_get_locale_files():
    locales = []
    path_domain = {
        'po': 'point_spectra_gui',
        os.path.join('po', 'countries'): 'point_spectra_gui-countries',
        os.path.join('po', 'attributes'): 'point_spectra_gui-attributes',
    }
    for path, domain in path_domain.items():
        for filepath in glob.glob(os.path.join(path, '*.po')):
            filename = os.path.basename(filepath)
            locale = os.path.splitext(filename)[0]
            locales.append((domain, locale, filepath))
    return locales


def _explode_path(path):
    """Return a list of components of the path (ie. "/a/b" -> ["a", "b"])"""
    components = []
    while True:
        (path, tail) = os.path.split(path)
        if tail == "":
            components.reverse()
            return components
        components.append(tail)


def _point_spectra_gui_packages():
    "Build a tuple containing each module under point_spectra_gui/"
    packages = []
    for subdir, dirs, files in os.walk("point_spectra_gui"):
        packages.append(".".join(_explode_path(subdir)))
    return tuple(sorted(packages))


args2 = {
    'name': PACKAGE_NAME,
    'version': __version__,
    'description': "A PDART-funded effort to design a spectral analysis tool for LIBS (and other) spectra",
    # long_description=long_description,
    'url': "https://github.com/USGS-Astrogeology/PySAT",
    'author': "Ryan B. Anderson, Nicholas Finch",
    'author_email': 'rbanderson@usgs.gov, ngf4@nau.edu',
    'license': "Public Domain",
    'keywords': 'MusicBrainz metadata tagger point_spectra_gui',
    'package_dir': {'point_spectra_gui': 'point_spectra_gui'},
    'packages': _point_spectra_gui_packages(),
    'locales': _point_spectra_gui_get_locale_files(),
    'data_files': [],
    'console_scripts': ['point_spectra_gui = point_spectra_gui.__main__:main'],
    'cmdclass': {
        'build': point_spectra_gui_build,
        'build_ui': point_spectra_gui_build_ui,
        'clean_ui': point_spectra_gui_clean_ui,
        'install': point_spectra_gui_install,
        'regen_pot_file': point_spectra_gui_regen_pot_file,
        'patch_version': point_spectra_gui_patch_version,
    },
    'install_requires': ['PyQt5'],
    'classifiers': [
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Topic :: Science :: Spectral/LIBS',
        'Topic :: Science :: Spectral/LIBS :: Analysis'
    ]
}
args.update(args2)


def generate_file(infilename, outfilename, variables):
    with open(infilename, "rt") as f_in:
        with open(outfilename, "wt") as f_out:
            f_out.write(f_in.read() % variables)


def contrib_plugin_files():
    plugin_files = {}
    dist_root = os.path.join("contrib", "plugins")
    for root, dirs, files in os.walk(dist_root):
        file_root = os.path.join('plugins', os.path.relpath(root, dist_root)) \
            if root != dist_root else 'plugins'
        for file in files:
            if file.endswith(".py"):
                if file_root in plugin_files:
                    plugin_files[file_root].append(os.path.join(root, file))
                else:
                    plugin_files[file_root] = [os.path.join(root, file)]
    data_files = [(x, sorted(y)) for x, y in plugin_files.items()]
    return sorted(data_files, key=lambda x: x[0])


def find_file_in_path(filename):
    for include_path in sys.path:
        file_path = os.path.join(include_path, filename)
        if os.path.exists(file_path):
            return file_path


# FIXME: this should check for the actual command ('install' vs. 'bdist_nsis', 'py2app', ...), not installed libraries
setup(**args)
