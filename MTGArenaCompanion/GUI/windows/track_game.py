import time
from threading import Thread
from time import time, sleep

from MTGArenaCompanion.GUI import GUI, Qt
from inspyre_toolbox import live_timer as timekeep

WIN_TITLE = 'Duel In Progress'


class MainGameWin(GUI):
    window = None

    game_timer = timekeep.Timer()

    pause_button_text = "Pause"

    blank_timer = '00:00:00'

    def __timer_frame_layout__(self):
        _ = [
            [
                Qt.Button(self.pause_button_text, key='PAUSE_BUTTON', visible=False),
                Qt.Text(self.blank_timer, size=(15, 4), font=('Helvetica', 18), justification='center',
                        key='TIMER_DISPLAY', pad=(10, 10),
                        relief=Qt.RELIEF_SUNKEN),
                Qt.Button('Reset', key='RESET_BUTTON', visible=False)
            ],
            [Qt.Button('Start Timer', enable_events=True, key='START_TIMER_BUTTON')]
        ]

        return _

    @staticmethod
    def __opp_frame__():
        _ = [
            [Qt.Text('Opponent\'s Name:'), Qt.InputText('Lamer', key='OPPONENT_NAME_INPUT')],
            [Qt.Text('Opponent\'s Final Life Total:'),
             Qt.InputText('20', key='OPPONENT_LIFE_INPUT', enable_events=True)],
            [Qt.Radio('Lost', group_id='WIN_LOSS_RADIO', enable_events=True, key='OPP_LOST_RADIO')],
            [
                Qt.Radio('Conceded', group_id='CONCEDE_DECK_RADIO', enable_events=True, key='OPP_CONCEDE_RADIO',
                         visible=False),
                Qt.Radio('Decked', group_id='CONCEDE_DECK_RADIO', enable_events=True, key='OPP_DECKED_RADIO',
                         visible=False)
            ],
        ]

        return _

    @staticmethod
    def __player_frame__():
        _ = [
            [Qt.Text('Your Final Life Total:'), Qt.InputText('20', key='PLAYER_LIFE_INPUT', enable_events=True)],
            [Qt.Radio('Lost', group_id='WIN_LOSS_RADIO', enable_events=True, key='PLAYER_LOSS_RADIO')],
            [
                Qt.Radio('Conceded', group_id='CONCEDE_DECK_RADIO', enable_events=True, key='PLAYER_CONCEDE_RADIO',
                         visible=False),
                Qt.Radio('Decked', group_id='CONCEDE_DECK_RADIO', enable_events=True, key='PLAYER_DECKED_RADIO',
                         visible=False)
            ],
        ]

        return _

    @staticmethod
    def __button_frame__():
        _ = [
            [Qt.Button('Cancel', enable_events=True, key='CANCEL_BUTTON'),
             Qt.Button('Submit', enable_events=True, key='SUBMIT_BUTTON', disabled=True)
             ],
        ]

        return _

    def __main_frame__(self):
        _ = [
            [Qt.Frame('', layout=self.__timer_frame_layout__(), )],
            [Qt.Frame('Opponent\'s Endgame State:', layout=self.__opp_frame__())],
            [Qt.Frame('Player\'s Endgame State:', layout=self.__player_frame__())],
            [Qt.Frame('', layout=self.__button_frame__())]
        ]

        return _

    def __layout__(self):
        _ = [
            [Qt.Frame('Duel Tracking', layout=self.__main_frame__())]
        ]

        return _

    def run(self):
        self.window = Qt.Window(WIN_TITLE, layout=self.__layout__(), alpha_channel=.8, return_keyboard_events=True,
                                grab_anywhere=True, no_titlebar=True, size=(800, 800))

        paused = True

        while True:
            event, vals = self.window.read(timeout=10)

            if event is None:
                self.window.close()
                break

            if event == 'START_TIMER_BUTTON':
                self.game_timer.run()
                paused = False
                self.window['START_TIMER_BUTTON'].update(visible=False)
                self.window['RESET_BUTTON'].update(visible=True)
                self.pause_button_text = 'Pause'
                self.window['PAUSE_BUTTON'].update(self.pause_button_text, visible=True)
                self.window.refresh()

            if 'timeout' not in event.lower():
                print(event)

            if not paused:
                self.window['TIMER_DISPLAY'].update(self.game_timer.get_elapsed())

            if event == 'RESET_BUTTON':
                paused = True
                i = 0

            if event == 'CANCEL_BUTTON':
                self.window.close()
                break

            if event == 'OPP_LOST_RADIO':
                self.window['OPP_CONCEDE_RADIO'].update(visible=True)
                paused = True if vals['OPP_LOST_RADIO'] else False


            self.window['PAUSE_BUTTON'].update('Start' if paused else 'Pause')
            if event == 'OPPONENT_LIFE_INPUT' or event == 'OPP_LOST_RADIO':
                if not vals['OPPONENT_LIFE_INPUT'] == '':
                    try:
                        if int(vals['OPPONENT_LIFE_INPUT']) >= 1 and vals['OPP_LOST_RADIO']:
                            self.window['OPP_DECKED_RADIO'].update(visible=True)
                            self.window['OPP_CONCEDE_RADIO'].update(visible=True)
                        else:
                            self.window['OPP_CONCEDE_RADIO'].update(visible=False)
                            self.window['OPP_DECKED_RADIO'].update(visible=False)
                    except ValueError:
                        self.window['OPPONENT_LIFE_INPUT'].update('0')

            if event == 'PAUSE_BUTTON':
                if not paused:
                    self.game_timer.pause()
                    paused = True
                else:
                    self.game_timer.unpause()
                    paused = False
