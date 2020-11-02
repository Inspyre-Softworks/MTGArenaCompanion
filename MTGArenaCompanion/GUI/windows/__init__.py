from MTGArenaCompanion.GUI import data_dir as DEFAULT_DATA_DIR

from MTGArenaCompanion.GUI.windows.start import StartWindow
from MTGArenaCompanion.GUI.windows.track_game import MainGameWin
from MTGArenaCompanion.GUI.windows.add_new_deck import AddDeckWin
from MTGArenaCompanion.GUI.windows.theme_win import ThemePrefWin
from MTGArenaCompanion.GUI.windows.logging_win import LoggingWin


from inspy_logger import getLogger

log_device = getLogger('MTGArenaCompanion.WinManifest')


class WinManifest(object):
    def __init__(self, data_dir=DEFAULT_DATA_DIR):
        self.start_window = StartWindow(log_device)
        self.game_window = MainGameWin(log_device)
        self.new_deck_window = AddDeckWin(data_dir)
        self.theme_man_window = ThemePrefWin(log_device)
        self.log_man_window = LoggingWin(log_device)
