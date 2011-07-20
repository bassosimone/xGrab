#
# Copyright (c) 2011 xGrab Development Team
#
# This file is part of xGrab
#
# xGrab is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# xGrab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with xGrab.  If not, see <http://www.gnu.org/licenses/>.
#

import logging
import sys

#
# Check for dependencies
#
try:
    import twisted
except ImportError, why:
    sys.stderr.write("Fatal: missing dependency: Twisted >= 11.0\n")
    sys.exit(1)

try:
    import pygtk
except ImportError, why:
    sys.stderr.write("Fatal: missing dependency: PyGtk >= 2.20\n")
    sys.exit(1)

#
# Really import Twisted and PyGtk.
#
from twisted.internet import gtk2reactor
gtk2reactor.install()

from twisted.internet import reactor

if __name__ == "__main__":
    sys.path.insert(0, '.')

from xgrab.gui import GtkGUI

# Setup a minimal logging
logging.basicConfig(filename='debug.log',
                    level=logging.DEBUG,
                    filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')

def main():

    # By default, run the GUI

    GtkGUI()
    reactor.run()

if __name__ == '__main__':
    main()
