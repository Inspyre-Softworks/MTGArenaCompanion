from configparser import ConfigParser
from os import makedirs
from pathlib import Path

import PySimpleGUIQt as Qt

from MTGArenaCompanion.GUI import GUI

from MTGArenaCompanion.lib import convert_dict_vals
from MTGArenaCompanion.lib.decks import REGULATION_LAND_TYPES, DeckMan

WIN_TITLE = 'Create New Deck'
LAND_TYPES = REGULATION_LAND_TYPES


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
            # Add a row to the deck composition frame that contains a spin-selector to input the number of cards in this deck, and label it with a Text element from PSG
            [
                Qt.Spin(range(1000), initial_value=self.card_total,
                        key='TOTAL_NUM', enable_events=True),
                Qt.Text('Number of cards in deck', key='TOTAL_NUM_LABEL'),
            ],

            # Add another row to the deck composition frame that contains a spin-selector (limited to the number of cards you state above) to tell how many of your total card count and a label stating as much
            [
                Qt.Spin(range(int(self.card_total / 2)), initial_value=int(self.card_total),
                        enable_events=True, key="TOTAL_LANDS"),
                Qt.Text("Number of land cards in this deck: ",
                        key="TOTAL_LANDS_LABEL")
            ],
        ]

        # Iterate over the 5 different land types so we can make check boxes for them without writing them all out. We go ahead and also add a plural 's' to every land-type except the "Plains" type
        for l_type in LAND_TYPES:
            if not l_type.lower() == "plains":
                plural = "s"
            else:
                plural = ""

            new_obj = [Qt.Spin([i for i in range(self.card_total)], initial_value=0, key=f"{l_type.upper()}_TOTAL", enable_events=True, visible=False),
                       Qt.Text(f"Number of {l_type + plural}", key=f"{l_type.upper()}_TOTAL_LABEL", visible=False)]

            _.append(new_obj)

        #     [Qt.Spin([i for i in range(self.card_total)], initial_value=0,
        #              key='SWAMP_TOTAL', enable_events=True, visible=False),
        #      Qt.Text('Number of swamps', key='SWAMP_TOTAL_LABEL', visible=False)],
        #     [Qt.Spin([i for i in range(self.card_total)], initial_value=0,
        #              key='ISLAND_TOTAL', enable_events=True, visible=False),
        #      Qt.Text('Number of islands', key='ISLAND_TOTAL_LABEL', visible=False)],
        #     [Qt.Spin([i for i in range(self.card_total)], initial_value=0,
        #              key='PLAINS_TOTAL', enable_events=True, visible=False),
        #      Qt.Text('Number of plains', key='PLAINS_TOTAL_LABEL', visible=False)],
        #     [Qt.Spin([i for i in range(self.card_total)], initial_value=0,
        #              key='MOUNTAIN_TOTAL', enable_events=True, visible=False),
        #      Qt.Text('Number of mountains', key='MOUNTAIN_TOTAL_LABEL', visible=False)],
        #     [Qt.Text('', key='TOTAL_LANDS', visible=False),
        #      Qt.Text('Lands in Total', visible=False, key='TOTAL_LANDS_LABEL')]
        # ]

        return _

    def __name_frame__(self):
        _ = [
            [Qt.InputText('', key='INPUT_DECK_NAME')]
        ]

        return _

    def __mana_frame__(self):
        _ = []

        for m_type in LAND_TYPES:
            _.append([Qt.Checkbox(
                m_type, key=f"{m_type.upper()}", enable_events=True)])

        return _

    def __layout__(self):
        main = [
            [Qt.Menu(self.main_menu)],
            [Qt.Frame('Deck Name', layout=self.__name_frame__())],
            [Qt.Frame('Mana Utilization', layout=self.__mana_frame__())],
            [Qt.Frame('Deck Composition', layout=self.__composition_frame__(
            ), key='DECK_COMP_FRAME')],
            [
                Qt.Button('OK', key='OK_BUTTON'),
                Qt.Button('Reset', key='RESET_BUTTON'),
                Qt.Button('Cancel', key='CANCEL_BUTTON')
            ]
        ]

        return main

    def run_window(self):

        all_land_types = LAND_TYPES

        self.add_active(WIN_TITLE)

        while self.check_if_active(WIN_TITLE):
            event, vals = self.window.read(timeout=10)

            if event == 'CANCEL_BUTTON' or event is None:
                print('User pressed the cancel button!')
                self.rem_active(WIN_TITLE)
                self.window.close()
                self.start_window.run_window()

                break

            if event in all_land_types:
                print(vals)
                for land in all_land_types:
                    self.window[f'{land}_TOTAL'].update(visible=vals[land])
                    self.window[f'{land}_TOTAL_LABEL'].update(
                        visible=vals[land])

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
                print(vals_obj)

                convert_dict_vals(vals_obj)

                print(vals_obj)

                parser = ConfigParser()
                parser.read_dict(vals_obj)
                print(parser.sections())
                with open(Path('~/Inspyre-Softworks/MTGArena-Companion/data/decks.ini').expanduser(), 'a') as config:
                    parser.write(config)

                for land_type in all_land_types:
                    if int(vals[f"{land_type.upper()}_TOTAL"]) >= 1:
                        self.mana_types += land_type.capitalize()

                self.rem_active(WIN_TITLE)
                self.start_window.run_window()

    def __init__(self, data_dir):
        super().__init__(data_dir)
        makedirs(data_dir, exist_ok=True)
        self.title = 'Add New Deck'
        self.deck_name = "Untitled Deck"
        self.card_total = 60
        self.land_total = 30
        self.mana_types = []
        self.window = Qt.Window('Deck Creator', layout=self.__layout__())
        print(self.log_name)
