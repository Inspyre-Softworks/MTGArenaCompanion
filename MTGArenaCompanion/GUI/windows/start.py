import PySimpleGUIQt as Qt
from MTGArenaCompanion.GUI import GUI
from MTGArenaCompanion.GUI.windows import add_new_deck

class StartWindow(GUI):

    @staticmethod
    def __layout__():
        _ = [
            [Qt.Button('Start New Match', key='START_NEW_BUTTON'), Qt.Button('Add a New Deck', key='NEW_DECK_BUTTON')],
            [Qt.Button('Preferences', key='PREFERENCES_BUTTON'), Qt.Button('Manage Decks', key='MANAGE_DECKS_BUTTON')],
            [Qt.Button('View Stats', key='VIEW_STATS_BUTTON'), Qt.Button('Quit', key='QUIT_BUTTON')]
        ]

        return _

    def __button_frame__(self):
        _ = [
            [Qt.Frame('Start Menu', layout=self.__layout__())]
        ]

        return _

    def run_window(self):
        window = Qt.Window('MTGArena Companion - Start Menu', layout=self.__button_frame__())

        buttons_not_implemented = ['START_NEW_BUTTON', 'PREFERENCES_BUTTON', 'MANAGE_DECKS_BUTTON', 'VIEW_STATS_BUTTON']

        while True:
            event, vals = window.read(timeout=100)

            if event is None or event == 'QUIT_BUTTON':
                break

            if event in buttons_not_implemented:
                self.not_yet_implemented_popup('This feature')

            if event == 'NEW_DECK_BUTTON':
                if self.check_if_active(add_new_deck.WIN_TITLE):
                    print("Can't reinitialize this window, it's already open!")
                else:
                    self.active_windows.append(add_new_deck.WIN_TITLE)
                    new_deck_win = add_new_deck.AddDeckWin()
                    window.hide()
                    new_deck_win.run_window()
                    self.rem_active(add_new_deck.WIN_TITLE)

            if


    def __init__(self):
        pass

start_win = StartWindow()
start_win.run_window()
