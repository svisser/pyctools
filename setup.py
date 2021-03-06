#!/usr/bin/env python
#  Pyctools - a picture processing algorithm development kit.
#  http://github.com/jim-easterbrook/pyctools
#  Copyright (C) 2014  Jim Easterbrook  jim@jim-easterbrook.me.uk
#
#  This program is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see
#  <http://www.gnu.org/licenses/>.

import os
from setuptools import setup, find_packages
import sys

packages = find_packages('src')

namespace_packages = []
for package in packages:
    init = os.path.join('src', package.replace('.', '/'), '__init__.py')
    for line in open(init).readlines():
        if 'declare_namespace' in line:
            # very likely a namespace package
            namespace_packages.append(package)
            break

console_scripts = []
for name in os.listdir('src/pyctools/tools'):
    base, ext = os.path.splitext(name)
    if name.startswith('_') or ext != '.py':
        continue
    console_scripts.append(
        'pyctools-{name} = pyctools.tools.{name}:main'.format(name=base))

long_description = open('README.rst').read()
url = 'https://github.com/jim-easterbrook/pyctools'

setup(name = 'pyctools.core',
      version = '0.0.0',
      author = 'Jim Easterbrook',
      author_email = 'jim@jim-easterbrook.me.uk',
      url = url,
      description = 'Picture processing algorithm development kit',
      long_description = long_description,
      classifiers = [
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Multimedia :: Video',
          'Topic :: Scientific/Engineering :: Image Recognition',
          'Topic :: Scientific/Engineering :: Visualization',
          ],
      license = 'GNU GPL',
      platforms = ['POSIX', 'MacOS', 'Windows'],
      packages = packages,
      namespace_packages = namespace_packages,
      package_dir = {'' : 'src'},
      entry_points = {
          'console_scripts' : console_scripts,
          },
      )
