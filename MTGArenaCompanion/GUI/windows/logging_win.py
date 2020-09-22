from MTGArenaCompanion.GUI import GUI, Qt


class LoggingWin(GUI):
    WIN_TITLE = 'Logging Settings'

    def __frame_layout_1__(self):
        radio_grp = 'LOGGING_LEVEL'
        _ = [
            [Qt.Radio('Debug', radio_grp, enable_events=True, key=radio_grp + '.debug'),
             Qt.Radio('Info', radio_grp, enable_events=True, key=radio_grp + '.info'),
             Qt.Radio('Warning', radio_grp, enable_events=True, key=radio_grp + '.warning')]
        ]
        return _

    def __layout__(self):
        _ = [
            [Qt.Frame('Log Output Level:', self.__frame_layout_1__())],
            [Qt.Button('Close', key='CLOSE_BUTTON', enable_events=True)]
        ]

        return _

    def run(self):
        window = Qt.Window(self.WIN_TITLE, self.__layout__())

        cur_lvl = None

        while True:
            event, vals = window.read(timeout=10)

            if event is None:
                break

            if event == 'CLOSE_BUTTON':
                break

            if not 'timeout'.upper() in event:
                print(event)
                print(vals)

            if vals['LOGGING_LEVEL.debug']:
                if not cur_lvl == 'debug':
                    self.log_device.adjust_level('debug')
                    cur_lvl = 'debug'

            if vals['LOGGING_LEVEL.info']:
                if not cur_lvl == 'info':
                    self.log_device.adjust_level('info')
                    cur_lvl = 'info'

            if vals['LOGGING_LEVEL.warning']:
                if not cur_lvl == 'warning':
                    self.log_device.adjust_level('warning')
                    cur_lvl = 'warning'
