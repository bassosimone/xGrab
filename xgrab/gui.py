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
