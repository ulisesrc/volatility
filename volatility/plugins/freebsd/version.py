# Volatility
# Copyright (C) 2019 Volatility Foundation
#
# This file is part of Volatility.
#
# Volatility is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Volatility is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Volatility.  If not, see <http://www.gnu.org/licenses/>.
#

import volatility.obj as obj
import volatility.plugins.freebsd.common as freebsd_common
from volatility.renderers import TreeGrid

class freebsd_version(freebsd_common.AbstractFreebsdCommand):
    """Dump FreeBSD version"""

    def __init__(self, config, *args, **kwargs):
        freebsd_common.AbstractFreebsdCommand.__init__(self, config, *args, **kwargs)

    def calculate(self):
        freebsd_common.set_plugin_members(self)
        version_addr = self.addr_space.profile.get_symbol('version')
        version = obj.Object('String', offset = version_addr, vm = self.addr_space, length = 256)
        yield version

    def unified_output(self, data):
        return TreeGrid([('Version', str)],
                        self.generator(data))

    def generator(self, data):
        for version in data:
            yield (0, [str(version)])