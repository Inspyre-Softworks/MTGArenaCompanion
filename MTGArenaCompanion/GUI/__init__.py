import PySimpleGUIQt as Qt

from inspy_logger import InspyLogger

from MTGArenaCompanion.GUI.menus import main_menu_struct


class GUI(object):
    import inspy_logger

    log_name = 'MTGArenaCompanion.GUI'
    log_device = InspyLogger(log_name, 'debug')
    log = log_device.start()

    active_windows = []
    main_menu = main_menu_struct

    def check_if_active(self, win_title):
        if win_title in self.active_windows:
            return True
        else:
            return False

    def add_active(self, win_title):
        self.active_windows.append(win_title)

    def rem_active(self, win_title):
        for win in self.active_windows:
            if win == win_title:
                self.active_windows.remove(win_title)

    @staticmethod
    def not_yet_implemented_popup(feature):
        title = 'Not Yet Implemented'
        statement = f"{feature} has yet to be implemented, check back soon!"
        Qt.PopupError(statement, title=title)

    def __init__(self):
        pass


gui = GUI()
gui.active_windows.append('SomeWindow')
if gui.check_if_active('SomeWindow'):
    print('Test successful')

gui.active_windows.append('AnotherWindow')
gui.active_windows.append('YetAnother')
print(gui.active_windows)
gui.rem_active('YetAnother')
print(gui.active_windows)

