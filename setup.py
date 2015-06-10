# -*- coding: utf-8 -*-

# Copyright 2013 django-htmlmin authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from setuptools import setup, find_packages
from htmlmin import __version__
import sys

PY_VERSION = sys.version_info[0], sys.version_info[1]
if PY_VERSION < (3, 0):
    README = open('README.rst').read()
else:
    README = open('README.rst', encoding='utf-8').read()

setup(
    name='django-htmlmin',
    version=__version__,
    description='html minify for django',
    long_description=README,
    author='CobraTeam',
    author_email='andrewsmedina@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    test_suite='nose.collector',
    install_requires=['argparse', 'beautifulsoup4', 'html5lib'],
    tests_require=['nose', 'coverage', 'django'],
    entry_points={
        'console_scripts': [
            'pyminify = htmlmin.commands:main',
        ],
    },
)
