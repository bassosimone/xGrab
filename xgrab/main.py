import logging
import sys

from twisted.internet import gtk2reactor
gtk2reactor.install()

from twisted.internet import reactor

sys.path.insert(0, '.')
from xgrab.gui import GtkGUI

# Setup a minimal logging
logging.basicConfig(filename='debug.log',
                    level=logging.DEBUG,
                    filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')

if __name__ == '__main__':

    # By default, run the GUI

    GtkGUI()
    reactor.run()
