# -*- coding: iso-8859-1 -*-

# Copyright (C) 2004 Juan M. Bello Rivas <rwx@synnergy.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""Testing framework.
"""

__revision__ = '$Id: __init__.py,v 1.1 2004/01/29 02:11:41 rwx Exp $'


import os
import unittest


curdir = os.path.split(__file__)[0]

istest = lambda x: x.startswith('test_') and x.endswith('.py')
gettest = lambda t: t[:-3]

modules = map(gettest, filter(istest, os.listdir(curdir)))

suites = []
loader = unittest.TestLoader()
for name in modules:
    module = __import__(name, globals(), locals(), [])
    # Discover and aggregate all the test suites.
    suites.append(loader.loadTestsFromModule(module))

suite = unittest.TestSuite(suites)
runner = unittest.TextTestRunner()
runner.run(suite)


# vim: ts=4 sw=4 et