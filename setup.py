from setuptools import setup, find_packages
from os import path
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
    install_requires=[
        'numpy',
        'pandas',
    ],
    extras_requires=[
        'inspect',
        'pickle',
        'PyQt4',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Spectral Analysis",
        "License :: Public Domain",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords="planetary io",
    packages=('point_spectra_gui', 'point_spectra_gui.ui', 'point_spectra_gui.ui_modules'),
)
