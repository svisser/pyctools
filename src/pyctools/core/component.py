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

"""Component base class.

Base class for all Pyctools components, i.e. objects designed to be
used in processing pipelines (or networks).

"""

__all__ = ['Component']

import logging

from guild.actor import *

from .config import ConfigMixin, ConfigInt
from .frame import Frame
from .metadata import Metadata
from .objectpool import ObjectPool

class Component(Actor, ConfigMixin):
    def __init__(self, with_outframe_pool=False):
        super(Component, self).__init__()
        ConfigMixin.__init__(self)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.with_outframe_pool = with_outframe_pool
        if self.with_outframe_pool:
            self.config.append(ConfigInt('outframe_pool_len', 3))

    def process_start(self):
        if self.with_outframe_pool:
            self.pool = ObjectPool(Frame, self.config['outframe_pool_len'])
            self.pool.bind("output", self, "new_out_frame")
            start(self.pool)

    def onStop(self):
        if self.with_outframe_pool:
            stop(self.pool)
