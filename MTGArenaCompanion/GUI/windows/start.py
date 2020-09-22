import PySimpleGUIQt as Qt
from MTGArenaCompanion.GUI import GUI
from MTGArenaCompanion.GUI.windows import add_new_deck, logging_win, timer

WIN_TITLE = 'Start Window'


class StartWindow(GUI):

    def __layout__(self):
        _ = [
            [Qt.Menu(self.main_menu, pad=(135, 135))],
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

        log_name = self.swin_logname + '.run_window'
        log = self.inspy_logger.getLogger(log_name)

        window = Qt.Window('MTGArena Companion - ' + WIN_TITLE, layout=self.__button_frame__(), force_toplevel=True,
                           keep_on_top=True)

        buttons_not_implemented = ['START_NEW_BUTTON', 'PREFERENCES_BUTTON', 'MANAGE_DECKS_BUTTON', 'VIEW_STATS_BUTTON']

        while True:
            event, vals = window.read(timeout=10)

            if not '__timeout__'.upper() in event:
                event = event.upper().replace(' ', '_')
                self.swin_log.debug(event)

            if event is None or 'QUIT' in event:
                if 'QUIT' in event:
                    self.swin_log.debug('Quit button or menu entry was pushed')
                    break

                break

            if event in buttons_not_implemented:
                self.not_yet_implemented_popup('This feature')

            if event == 'NEW_DECK_BUTTON':
                if self.check_if_active(add_new_deck.WIN_TITLE):
                    print("Can't reinitialize this window, it's already open!")
                else:
                    log.debug(f'Adding {add_new_deck.WIN_TITLE} to active window manifest')
                    self.active_windows.append(add_new_deck.WIN_TITLE)
                    new_deck_win = add_new_deck.AddDeckWin()
                    log.debug(f'Hiding {WIN_TITLE}')
                    window.hide()
                    log.debug(f'Running {add_new_deck.WIN_TITLE}')
                    new_deck_win.run_window()
                    log.debug(f'Exited {add_new_deck.WIN_TITLE}')
                    log.debug(f'Removing {add_new_deck.WIN_TITLE} from active window manifest')
                    self.rem_active(add_new_deck.WIN_TITLE)
                    log.debug(f'Showing {WIN_TITLE} again')
                    window.un_hide()

            if event == 'LOGGING':
                if self.check_if_active(logging_win.LoggingWin.WIN_TITLE):
                    print('It is already open')
                else:
                    self.active_windows.append(logging_win.LoggingWin.WIN_TITLE)
                    window.hide()
                    log_win = logging_win.LoggingWin()
                    log_win.run()
                    self.rem_active(log_win.WIN_TITLE)
                    window.un_hide()

            if event == 'TIMER':
                if not self.check_if_active(timer.WIN_TITLE):
                    self.add_active(timer.WIN_TITLE)
                    duel_track_win = timer.MainGameWin()
                    window.hide()
                    duel_track_win.run()
                    self.rem_active(timer.WIN_TITLE)
                    window.un_hide()

    def __init__(self):
        self.swin_logname = self.log_name + '.' + WIN_TITLE.replace(' ', '')
        self.swin_log = self.inspy_logger.getLogger(self.swin_logname)

