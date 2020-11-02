from pathlib import Path
from configparser import ConfigParser
from os import makedirs

REGULATION_LAND_TYPES = ["Swamp", "Island", "Plains", "Forest"]


class ExistingManifestError(Exception):
    def __init__(self, message):
        self.message = message


class DeckMan(object):
    def __init__(self, datapath):
        db_name = 'deck_manifest.ini'
        decks = ConfigParser()
        self.db_path = str(
            Path(datapath).expanduser().resolve()) + '/' + db_name

        if Path(self.db_path).exists():
            decks = decks.read(self.db_path)
        else:
            decks = None

        self.avail_land_types = REGULATION_LAND_TYPES

        self.decks = decks

    def create_manifest(self, deck_name, deck_data):
        if self.decks is not None:
            raise ExistingManifestError(
                message=f"There's already a manifest at {self.db_path}")

        fmt_name = deck_data['name'].replace(' ', '_').capitalize()

        land_total = int(deck_data['SWAMP_TOTAL']) + int(deck_data['ISLAND_TOTAL']) + int(
            deck_data['PLAINS_TOTAL']) + int(deck_data['MOUNTAIN_TOTAL'])

        deck_struct = {
            fmt_name: {
                'deck_name': deck_data['INPUT_DECK_NAME'],
                'card_total': deck_data['TOTAL_NUM'],
                'land_total': deck_data['lands'],
                'land_types': deck_data['mana_types'],
                'swamps': deck_data['SWAMP_TOTAL'],
                'islands': deck_data['ISLAND_TOTAL'],
                'mountains': deck_data['MOUNTAIN_TOTAL'],
                'plains': deck_data['PLAINS_TOTAL'],
                'colorless': 0,
                'usage_time': 0,
                'wins': 0,
                'losses': 0,
                'draws': 0,
                'longest_streak': 0,

            }

        }

        self.decks = ConfigParser()
        self.decks.read_dict(deck_struct)

        return self.decks

    def write_manifest(self, deck_data):
        with open(self.db_path, 'w') as file:
            deck_data.write(file)

    def load_manifest(self):
        parser = ConfigParser()
        parser.read(self.db_path)

        self.decks = parser

        return self.decks
