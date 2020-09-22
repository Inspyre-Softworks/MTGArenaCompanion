
class MTGACApp(object):

    runtime_args = None
    # from MTGArenaCompanion.GUI.windows.start import StartWindow
    # from MTGArenaCompanion.lib.arg_parse import ArgParser

    start_window = None
    log_device = None

    def inspect_self(self):
        print(dir(self))