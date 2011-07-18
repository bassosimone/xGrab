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

import gtk


class GtkGUI:

    """ xGrab GUI """

    def __init__(self):

        """ Initialize the GUI """

        glade_file = 'main.glade'
        builder = gtk.Builder()
        builder.add_from_file(glade_file)
        builder.connect_signals(self)

    @classmethod
    def gtk_main_quit(cls, error):

        """ Handle quit event """

        gtk.main_quit()
