from os import path
from setuptools import setup, find_packages

import point_spectra_gui

VERSION = point_spectra_gui.__version__
here = path.abspath(path.dirname(__file__))

# TODO PyPi requires a README.rst file, not a README.md
# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name="Point Spectra GUI",
    version=VERSION,
    description="A PDART-funded effort to design a spectral analysis tool for LIBS (and other) spectra",
    # long_description=long_description,
    url="https://github.com/USGS-Astrogeology/PySAT",
    author="Ryan B. Anderson, Nicholas Finch",
    author_email='rbanderson@usgs.gov, ngf4@nau.edu',
    license="Public Domain",
    entry_points={
        'console_scripts': [
            'point_spectra_gui = point_spectra_gui.__main__:main'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import datetime
import glob
import os
import re
import sys
import subprocess
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
from setuptools import setup, Command, Extension


PACKAGE_NAME = "Point Spectra GUI"

ext_modules = [
    Extension('point_spectra_gui.util._astrcmp', sources=['point_spectra_gui/util/_astrcmp.c']),
]

py2app_exclude_modules = [
    'pydoc',
    'PyQt5.QtDeclarative', 'PyQt5.QtDesigner', 'PyQt5.QtHelp', 'PyQt5.QtMultimedia',
    'PyQt5.QtOpenGL', 'PyQt5.QtScript', 'PyQt5.QtScriptTools', 'PyQt5.QtSql', 'PyQt5.QtSvg',
    'PyQt5.QtTest', 'PyQt5.QtWebKit', 'PyQt5.QtXml', 'PyQt5.QtXmlPatterns', 'PyQt5.phonon'
]

# sockets module, however not excluded from py2exe should not be used in point_spectra_gui. Instead
# the QtNetwork module should be used. sockets module was removed from the excluded list
# to support bundled plugins on platforms it is not available.
py2exe_exclude_modules = [
    'select',
]

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


class point_spectra_gui_build_locales(Command):
    description = 'build locale files'
    user_options = [
        ('build-dir=', 'd', "directory to build to"),
        ('inplace', 'i', "ignore build-lib and put compiled locales into the 'locale' directory"),
    ]

    def initialize_options(self):
        self.build_dir = None
        self.inplace = 0

    def finalize_options(self):
        self.set_undefined_options('build', ('build_locales', 'build_dir'))
        self.locales = self.distribution.locales

    def run(self):
        for domain, locale, po in self.locales:
            if self.inplace:
                path = os.path.join('locale', locale, 'LC_MESSAGES')
            else:
                path = os.path.join(self.build_dir, locale, 'LC_MESSAGES')
            mo = os.path.join(path, '%s.mo' % domain)
            self.mkpath(path)
            self.spawn(['msgfmt', '-o', mo, po])

Distribution.locales = None


class point_spectra_gui_install_locales(Command):
    description = "install locale files"
    user_options = [
        ('install-dir=', 'd', "directory to install locale files to"),
        ('build-dir=', 'b', "build directory (where to install from)"),
        ('force', 'f', "force installation (overwrite existing files)"),
        ('skip-build', None, "skip the build steps"),
    ]
    boolean_options = ['force', 'skip-build']

    def initialize_options(self):
        self.install_dir = None
        self.build_dir = None
        self.force = 0
        self.skip_build = None
        self.outfiles = []

    def finalize_options(self):
        self.set_undefined_options('build', ('build_locales', 'build_dir'))
        self.set_undefined_options('install',
                                   ('install_locales', 'install_dir'),
                                   ('force', 'force'),
                                   ('skip_build', 'skip_build'),
                                  )

    def run(self):
        if not self.skip_build:
            self.run_command('build_locales')
        self.outfiles = self.copy_tree(self.build_dir, self.install_dir)

    def get_inputs(self):
        return self.locales or []

    def get_outputs(self):
        return self.outfiles


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
        self.install_locales = None
        self.localedir = None
        self.disable_autoupdate = None
        self.disable_locales = None

    def finalize_options(self):
        install.finalize_options(self)
        if self.install_locales is None:
            self.install_locales = '$base/share/locale'
            self._expand_attrs(['install_locales'])
        self.install_locales = os.path.normpath(self.install_locales)
        self.localedir = self.install_locales
        # can't use set_undefined_options :/
        self.distribution.get_command_obj('build').localedir = self.localedir
        self.distribution.get_command_obj('build').disable_autoupdate = self.disable_autoupdate
        if self.root is not None:
            self.change_roots('locales')
        if self.disable_locales is None:
            self.sub_commands.append(('install_locales', None))

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
        self.build_locales = None
        self.localedir = None
        self.disable_autoupdate = None
        self.disable_locales = None

    def finalize_options(self):
        build.finalize_options(self)
        if self.build_locales is None:
            self.build_locales = os.path.join(self.build_base, 'locale')
        if self.localedir is None:
            self.localedir = '/usr/share/locale'
        if self.disable_autoupdate is None:
            self.disable_autoupdate = False
        if self.disable_locales is None:
            self.sub_commands.append(('build_locales', None))

    def run(self):
        if 'bdist_nsis' not in sys.argv:  # somebody shoot me please
            log.info('generating scripts/%s from scripts/point_spectra_gui.in', PACKAGE_NAME)
            generate_file('scripts/point_spectra_gui.in', 'scripts/' + PACKAGE_NAME, {'localedir': self.localedir, 'autoupdate': not self.disable_autoupdate})
        build.run(self)


def py_from_ui(uifile):
    return "ui_%s.py" % os.path.splitext(os.path.basename(uifile))[0]


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
            uic.compileUi(uifile, tmp)
            source = tmp.getvalue()
            rc = re.compile(r'\n\n#.*?(?=\n\n)', re.MULTILINE|re.DOTALL)
            comment = ("\n\n# Automatically generated - don't edit.\n"
                       "# Use `python setup.py %s` to update it."
                       % _get_option_name(self))
            for r in list(_translate_re):
                source = r.sub(r'_(\1)', source)
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

        from resources import compile, makeqrc
        makeqrc.main()
        compile.main()


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


class point_spectra_gui_get_po_files(Command):
    description = "Retrieve po files from transifex"
    minimum_perc_default = 5
    user_options = [
        ('minimum-perc=', 'm',
         "Specify the minimum acceptable percentage of a translation (default: %d)" % minimum_perc_default)
    ]

    def initialize_options(self):
        self.minimum_perc = self.minimum_perc_default

    def finalize_options(self):
        self.minimum_perc = int(self.minimum_perc)

    def run(self):
        if tx_executable is None:
            sys.exit('Transifex client executable (tx) not found.')
        txpull_cmd = [
            tx_executable,
            'pull',
            '--force',
            '--all',
            '--minimum-perc=%d' % self.minimum_perc
        ]
        self.spawn(txpull_cmd)


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


class point_spectra_gui_update_constants(Command):
    description = "Regenerate attributes.py and countries.py"
    user_options = [
        ('skip-pull', None, "skip the tx pull steps"),
    ]
    boolean_options = ['skip-pull']

    def initialize_options(self):
        self.skip_pull = None

    def finalize_options(self):
        self.locales = self.distribution.locales

    def run(self):
        if tx_executable is None:
            sys.exit('Transifex client executable (tx) not found.')

        from babel.messages import pofile

        if not self.skip_pull:
            txpull_cmd = [
                tx_executable,
                'pull',
                '--force',
                '--resource=musicbrainz.attributes,musicbrainz.countries',
                '--source',
                '--language=none',
            ]
            self.spawn(txpull_cmd)

        countries = dict()
        countries_potfile = os.path.join('po', 'countries', 'countries.pot')
        isocode_comment = 'iso.code:'
        with open(countries_potfile, 'rb') as f:
            log.info('Parsing %s' % countries_potfile)
            po = pofile.read_po(f)
            for message in po:
                if not message.id or not isinstance(message.id, str):
                    continue
                for comment in message.auto_comments:
                    if comment.startswith(isocode_comment):
                        code = comment.replace(isocode_comment, '')
                        countries[code] = message.id
            if countries:
                self.countries_py_file(countries)
            else:
                sys.exit('Failed to extract any country code/name !')

        attributes = dict()
        attributes_potfile = os.path.join('po', 'attributes', 'attributes.pot')
        extract_attributes = (
            'DB:cover_art_archive.art_type/name',
            'DB:medium_format/name',
            'DB:release_group_primary_type/name',
            'DB:release_group_secondary_type/name',
        )
        with open(attributes_potfile, 'rb') as f:
            log.info('Parsing %s' % attributes_potfile)
            po = pofile.read_po(f)
            for message in po:
                if not message.id or not isinstance(message.id, str):
                    continue
                for loc, pos in message.locations:
                    if loc in extract_attributes:
                        attributes["%s:%03d" % (loc, pos)] = message.id
            if attributes:
                self.attributes_py_file(attributes)
            else:
                sys.exit('Failed to extract any attribute !')

    def countries_py_file(self, countries):
        header = ("# -*- coding: utf-8 -*-\n"
                  "# Automatically generated - don't edit.\n"
                  "# Use `python setup.py {option}` to update it.\n"
                  "\n"
                  "RELEASE_COUNTRIES = {{\n")
        line   =  "    '{code}': '{name}',\n"
        footer =  "}}\n"
        filename = os.path.join('point_spectra_gui', 'const', 'countries.py')
        with open(filename, 'w') as countries_py:
            def write(s, **kwargs):
                countries_py.write(s.format(**kwargs))

            write(header, option=_get_option_name(self))
            for code, name in sorted(countries.items(), key=lambda t: t[0]):
                write(line, code=code, name=name.replace("'", "\\'"))
            write(footer)
            log.info("%s was rewritten (%d countries)" % (filename,
                                                          len(countries)))

    def attributes_py_file(self, attributes):
        header = ("# -*- coding: utf-8 -*-\n"
                  "# Automatically generated - don't edit.\n"
                  "# Use `python setup.py {option}` to update it.\n"
                  "\n"
                  "MB_ATTRIBUTES = {{\n")
        line   =  "    '{key}': '{value}',\n"
        footer =  "}}\n"
        filename = os.path.join('point_spectra_gui', 'const', 'attributes.py')
        with open(filename, 'w') as attributes_py:
            def write(s, **kwargs):
                attributes_py.write(s.format(**kwargs))

            write(header, option=_get_option_name(self))
            for key, value in sorted(attributes.items(), key=lambda i: i[0]):
                write(line, key=key, value=value.replace("'", "\\'"))
            write(footer)
            log.info("%s was rewritten (%d attributes)" % (filename,
                                                           len(attributes)))


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
        (path,tail) = os.path.split(path)
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
    'description': 'The next generation MusicBrainz tagger',
    'keywords': 'MusicBrainz metadata tagger point_spectra_gui',
    'url': 'https://point_spectra_gui.musicbrainz.org/',
    'package_dir': {'point_spectra_gui': 'point_spectra_gui'},
    'packages': _point_spectra_gui_packages(),
    'locales': _point_spectra_gui_get_locale_files(),
    'ext_modules': ext_modules,
    'data_files': [],
    'cmdclass': {
        'test': point_spectra_gui_test,
        'build': point_spectra_gui_build,
        'build_locales': point_spectra_gui_build_locales,
        'build_ui': point_spectra_gui_build_ui,
        'clean_ui': point_spectra_gui_clean_ui,
        'install': point_spectra_gui_install,
        'install_locales': point_spectra_gui_install_locales,
        'update_constants': point_spectra_gui_update_constants,
        'get_po_files': point_spectra_gui_get_po_files,
        'regen_pot_file': point_spectra_gui_regen_pot_file,
        'patch_version': point_spectra_gui_patch_version,
    },
    'scripts': ['scripts/' + PACKAGE_NAME],
    'install_requires': ['PyQt5', 'mutagen'],
    'classifiers': [
    'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS',
    'Operating System :: POSIX :: Linux',
    'Topic :: Multimedia :: Sound/Audio',
    'Topic :: Multimedia :: Sound/Audio :: Analysis'
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


try:
    from py2exe.build_exe import py2exe

    class bdist_nsis(py2exe):

        def run(self):
            generate_file('scripts/point_spectra_gui.py2exe.in', 'scripts/point_spectra_gui', {})
            self.distribution.data_files.append(
                ("", ["discid.dll", "fpcalc.exe", "msvcr90.dll", "msvcp90.dll"]))
            for locale in self.distribution.locales:
                self.distribution.data_files.append(
                    ("locale/" + locale[1] + "/LC_MESSAGES",
                     ["build/locale/" + locale[1] + "/LC_MESSAGES/" + locale[0] + ".mo"]))
            self.distribution.data_files.append(
                ("imageformats", [find_file_in_path("PyQt5/plugins/imageformats/qgif4.dll"),
                                  find_file_in_path("PyQt5/plugins/imageformats/qjpeg4.dll"),
                                  find_file_in_path("PyQt5/plugins/imageformats/qtiff4.dll")]))
            self.distribution.data_files.append(
                ("accessible", [find_file_in_path("PyQt5/plugins/accessible/qtaccessiblewidgets4.dll")]))
            self.distribution.data_files += contrib_plugin_files()

            py2exe.run(self)
            print("*** creating the NSIS setup script ***")
            pathname = r"installer\point_spectra_gui-setup.nsi"
            generate_file(pathname + ".in", pathname,
                          {'name': 'MusicBrainz point_spectra_gui',
                           'version': __version__,
                           'description': 'The next generation MusicBrainz tagger.',
                           'url': 'https://point_spectra_gui.musicbrainz.org/', })
            print("*** compiling the NSIS setup script ***")
            subprocess.call([self.find_nsis(), pathname])

        def find_nsis(self):
            import _winreg
            with _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "Software\\NSIS") as reg_key:
                nsis_path = _winreg.QueryValueEx(reg_key, "")[0]
                return os.path.join(nsis_path, "makensis.exe")

    args['cmdclass']['bdist_nsis'] = bdist_nsis
    args['windows'] = [{
        'script': 'scripts/point_spectra_gui',
        'icon_resources': [(1, 'point_spectra_gui.ico')],
    }]
    args['options'] = {
        'bdist_nsis': {
            # mimetypes is necessary for the videotools plugin
            'includes': ['json', 'sip', 'mimetypes'] + [e.name for e in ext_modules],
            'excludes': exclude_modules + py2exe_exclude_modules,
            'optimize': 2,
        },
    }
except ImportError:
    py2exe = None


def find_file_in_path(filename):
    for include_path in sys.path:
        file_path = os.path.join(include_path, filename)
        if os.path.exists(file_path):
            return file_path


# FIXME: this should check for the actual command ('install' vs. 'bdist_nsis', 'py2app', ...), not installed libraries
setup(**args)