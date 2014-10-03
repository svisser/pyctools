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

"""Pyctools "Frame" class.

This is a fairly free-form container, but every Frame object must have:

* a frame number
* a list of zero or more data items, which may themselves be Frames
* a type description string, such as "RGB"
* a Metadata item

"""

from __future__ import print_function

import sys
import time

import numpy
import PIL

class Metadata(object):
    def copy(self, other):
        pass

class Frame(object):
    def __init__(self):
        self.frame_no = -1
        self.data = []
        self.type = 'empty'
        self.metadata = Metadata()

    def initialise(self, other):
        self.frame_no = other.frame_no
        self.metadata.copy(other.metadata)

    def as_numpy(self):
        result = []
        for data in self.data:
            if isinstance(data, numpy.ndarray):
                result.append(data)
            elif isinstance(data, PIL.Image):
                result.append(numpy.ndarray(data))
            else:
                raise RuntimeError(
                    'Cannot convert "%s" to numpy' % data.__class__.__name__)
        return result

    def as_PIL(self):
        result = []
        for data in self.data:
            if isinstance(data, numpy.ndarray):
                result.append(PIL.Image.fromarray(data))
            elif isinstance(data, PIL.Image):
                result.append(data)
            else:
                raise RuntimeError(
                    'Cannot convert "%s" to PIL' % data.__class__.__name__)
        return result
