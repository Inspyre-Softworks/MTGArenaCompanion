from MTGArenaCompanion.GUI import GUI, Qt, inspy_logger
import time

WIN_TITLE = 'Duel Tracker'


class MainGameWin(GUI):

    window=None

    pause_button_text = "Start"

    def __layout__(self):
        _ = [[Qt.Text(size=(15, 4), font=('Helvetica', 20), justification='center', key='TIMER_DISPLAY')],
             [Qt.Button(self.pause_button_text, key='PAUSE_BUTTON'),
              Qt.Button('Reset', key='RESET_BUTTON'),
              Qt.Exit(button_color=('white', 'firebrick4'), key='EXIT_BUTTON')]]

        return _

    def run(self):
        self.window = Qt.Window(WIN_TITLE, layout=self.__layout__())

        i = 0

        paused = True

        start_time = int(round(time.time() * 100))

        while True:
            event, vals = self.window.read(timeout=10)

            self.window['TIMER_DISPLAY'].update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))

            if not paused:
                i += 1
                if event == 'PAUSE_BUTTON':
                    paused = True
            else:
                if event == 'PAUSE_BUTTON':
                    paused = False

            if event == 'RESET_BUTTON':
                paused = True
                i = 0

            if event is None:
                self.window.close()
                break

            if event == 'EXIT_BUTTON':
                self.window.close()
                break

            self.window['PAUSE_BUTTON'].update('Start' if paused else 'Pause')



# Basic timer in PQt

# def Timer():
#     Qt.theme('Dark')
#
#     paused = True
#
#     if paused:
#         pause_button_text = 'Start'
#     else:
#         pause_button_text = 'Pause'
#
#     Qt.set_options(element_padding=(0, 0))
#     form_rows = [[Qt.Text(size=(8, 2), font=('Helvetica', 20),
#                        justification='center', key='text')],
#                  [Qt.Button(pause_button_text, key='-RUN-PAUSE-'),
#                  Qt.Button('Reset'),
#                  Qt.Exit(button_color=('white', 'firebrick4'))]]
#     window = Qt.Window('Running Timer', form_rows,
#                        no_titlebar=True, auto_size_buttons=False)
#     i = 0
#
#     start_time = int(round(time.time() * 100))
#
#     while True:
#         # This is the code that reads and updates your window
#         button, values = window.read(timeout=10)
#         window['text'].update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
#
#         if values is None or button == 'Exit':
#             print(window['text'].get())
#             window.close()
#             break
#
#         if button == 'Reset':
#             paused = True
#             window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')
#             i = 0
#
#         elif button == '-RUN-PAUSE-':
#             paused = not paused
#             window['-RUN-PAUSE-'].update('Run' if paused else 'Pause')
#
#         if not paused:
#             i += 1
