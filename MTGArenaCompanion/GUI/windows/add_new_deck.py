from configparser import ConfigParser
from os import makedirs
from pathlib import Path

import PySimpleGUIQt as Qt

from MTGArenaCompanion.GUI import GUI

WIN_TITLE = 'Create New Deck'


class AddDeckWin(GUI):
    max_num_cards = 1000
    land_types = []
    win_title = WIN_TITLE

    @staticmethod
    def __divide_by_half__(initial_number: int):
        end = initial_number / 2

        return end

    def __composition_frame__(self):
        _ = [
            [Qt.Spin(range(1000), initial_value=self.card_total, key='TOTAL_NUM', enable_events=True),
             Qt.Text('Number of cards in deck', key='TOTAL_NUM_LABEL')],
            [Qt.Spin([i for i in range(self.card_total)], initial_value=0,
                     key='SWAMP_TOTAL', enable_events=True, visible=False),
             Qt.Text('Number of swamps', key='SWAMP_TOTAL_LABEL', visible=False)],
            [Qt.Spin([i for i in range(self.card_total)], initial_value=0,
                     key='ISLAND_TOTAL', enable_events=True, visible=False),
             Qt.Text('Number of islands', key='ISLAND_TOTAL_LABEL', visible=False)],
            [Qt.Spin([i for i in range(self.card_total)], initial_value=0,
                     key='PLAINS_TOTAL', enable_events=True, visible=False),
             Qt.Text('Number of plains', key='PLAINS_TOTAL_LABEL', visible=False)],
            [Qt.Spin([i for i in range(self.card_total)], initial_value=0,
                     key='MOUNTAIN_TOTAL', enable_events=True, visible=False),
             Qt.Text('Number of mountains', key='MOUNTAIN_TOTAL_LABEL', visible=False)],
            [Qt.Text('', key='TOTAL_LANDS', visible=False),
             Qt.Text('Lands in Total', visible=False, key='TOTAL_LANDS_LABEL')]
        ]

        return _

    def __name_frame__(self):
        _ = [
            [Qt.InputText('', key='INPUT_DECK_NAME')]
        ]

        return _

    def __mana_frame__(self):
        _ = [
            [Qt.Checkbox('Swamp', key='SWAMP', enable_events=True),
             Qt.Checkbox('Plains', key='PLAINS', enable_events=True)],
            [Qt.Checkbox('Island', key='ISLAND', enable_events=True),
             Qt.Checkbox('Mountain', key='MOUNTAIN', enable_events=True)]
        ]

        return _

    def __layout__(self):
        main = [
            [Qt.Menu(self.main_menu)],
            [Qt.Frame('Deck Name', layout=self.__name_frame__())],
            [Qt.Frame('Mana Utilization', layout=self.__mana_frame__())],
            [Qt.Frame('Deck Composition', layout=self.__composition_frame__(), key='DECK_COMP_FRAME')],
            [
                Qt.Button('OK', key='OK_BUTTON'),
                Qt.Button('Reset', key='RESET_BUTTON'),
                Qt.Button('Cancel', key='CANCEL_BUTTON')
            ]
        ]

        return main

    def run_window(self):

        all_land_types = ['SWAMP', 'MOUNTAIN', 'ISLAND', 'PLAINS']

        while self.check_if_active(WIN_TITLE):
            event, vals = self.window.read(timeout=10)

            if event == 'CANCEL_BUTTON' or event is None:
                print('User pressed the cancel button!')
                self.rem_active(WIN_TITLE)
                self.window.close()

                break

            if event in all_land_types:
                print(vals)
                for land in all_land_types:
                    self.window[f'{land}_TOTAL'].update(visible=vals[land])
                    self.window[f'{land}_TOTAL_LABEL'].update(visible=vals[land])

            if event == 'TOTAL_NUM':
                self.card_total = vals['TOTAL_NUM']
                total_halved = self.__divide_by_half__(self.card_total)
                self.window['TOTAL_LANDS'].update(total_halved)
                self.window['LAND_NUM_OUT'].update(f'/{self.card_total}')

            if event == 'TOTAL_LANDS':
                self.land_total = vals['TOTAL_LANDS']
                self.window['LAND_NUM_OUT'].update(f'/{self.card_total}')

            if event == 'OK_BUTTON':
                print(vals)
                vals_obj = {
                    vals['INPUT_DECK_NAME'].replace(' ', '_').upper() + '.DECK': vals
                }
                parser = ConfigParser()
                parser.read_dict(vals_obj)
                print(parser.sections())
                with open(Path('~/Inspyre-Softworks/MTGArena-Companion/data/decks.ini').expanduser(), 'a') as config:
                    parser.write(config)

    def __init__(self):
        data_dir = Path('~/Inspyre-Softworks/MTGArena-Companion/data').expanduser()
        makedirs(data_dir, exist_ok=True)
        self.title = 'Add New Deck'
        self.card_total = 60
        self.land_total = 30
        self.window = Qt.Window('Deck Creator', layout=self.__layout__())
        print(self.log_name)
