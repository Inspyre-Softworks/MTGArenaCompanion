# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from MTGArenaCompanion import MTGACApp
import inspy_logger
from inspy_logger import InspyLogger


class MTGArenaCompanion(MTGACApp):

    arg_parser = None
    arguments = None
    log = None

    def parse_arguments(self):
        from MTGArenaCompanion.lib.arg_parse import ArgParser

        self.arg_parser = ArgParser()
        self.arg_parser.parse()
        self.arguments = self.arg_parser.arguments

    def start_gui(self):
        from MTGArenaCompanion.GUI.windows.start import StartWindow

        self.start_window = StartWindow()
        self.start_window.run_window()

    def __init__(self):
        super().__init__()
        var = self.log_device
        print(self.log_device)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = MTGArenaCompanion()
    app.parse_arguments()
    app.log_device = InspyLogger('MTGArenaCompanion', app.arguments.log_level)
    app.log = app.log_device.start()
    print(app.inspect_self())

    app.start_gui()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
