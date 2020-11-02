#!python
"""

MTGArena Companion

MTGArena Companion is an application developed to assist you in keeping track of vital MTGA win/loss data, broken down
by deck. Planned features include (but are not limited to):

* Works on Windows 10 & Ubuntu Linux (tested)
* Store general (but still useful) data about your in-game decks including:
  * Deck name
  * Number of cards in the deck
    * (including a count of each mana color)
* Track data on each of your match-ups including:
  * Each players ending life total;
    * Did the match end due to a player conceding? Getting decked?
      * If you conceded, you're presented with a couple options as to why you might have done so:
      * Mana flood
      * Mana drought
      * No seen route to survival
      * Bio (reasons not related to the game, just couldn't finish)
        * Computer failure
      * Non-Starter (inability to get a hand you can start the game with)
* Time spent playing
* Use the deck information associated with the game you're tracking so you can keep track of things such as:
  * Optimal land/non-land ratios
  * Winning averages per deck
  * Average time in-duel
* Parse and use this collected data in meaningful way to help us get better at MTGArena and fine-tune your decks

****

Author: Taylor-Jayde Blackstone <t.blackstone@inspyre.tech>
Author Homepage: https://softworks.inspyre.tech
Version: 1.0 dev3
Source URL: https://github.com/Inspyre-Softworks/MTGArenaCompanion
Wiki URL: https://github.com/Inspyre-Softworks/MTGArenaCompanion/wiki
Issue URL: https://github.com/Inspyre-Softworks/MTGArenaCompanion/issues

"""
from MTGArenaCompanion import MTGACApp
import inspy_logger
from inspy_logger import InspyLogger
from inspyred_print import Color as color, Format as format, Effects as fx


log_name = 'MTGArenaCompanion.App'


# def ident(logger):
#     bl = color.blue
#     gr = color.green
#     ye = color.yellow
#     bo = format.bold
#     en = format.end_mod
#
#
#     lines = [
#         f"{bo}{ye}****{en}{bl}Logger Started for {log_name}{en}{bo}{ye}****{en}\n",
#         f"{bo}{ye}*************************************{en}\n",
#         f"{bo}{ye}**{en} {bo}{bl}Project Lead:{en} {gr}Taylor Blackstone{en} {ye}{bo}**{en}\n",
#         f"{bo}{ye}**{en} {bo}{bl}Version:{en} {gr}1.0 {bo}{color.red}(DEVELOPMENT){en}      {bo}{ye}**{en}\n",
#         f"{bo}{ye}**{en} {bo}{bl}Ident Date:{en} {gr}10/19/2020{en}          {en}{bo}{ye}**\n",
#     ]
#
#     return lines


class MTGArenaCompanion(MTGACApp):

    arg_parser = None
    arguments = None

    log_device = InspyLogger(log_name, 'debug')
    if not log_device.started:
        log = log_device.start()

    def parse_arguments(self):
        from MTGArenaCompanion.lib.arg_parse import ArgParser

        self.arg_parser = ArgParser()
        self.arg_parser.parse()
        self.arguments = self.arg_parser.arguments

    def start_gui(self):
        from MTGArenaCompanion.GUI.windows.start import StartWindow

        self.start_window = StartWindow()
        self.start_window.run_window()

    def __init__(self):
        super().__init__()
        var = self.log_device
        print(self.log_device)


if __name__ == '__main__':
    app = MTGArenaCompanion()
    app.parse_arguments()
    app.log_device = InspyLogger('MTGArenaCompanion', app.arguments.log_level)
    app.log = app.log_device.start()

    app.start_gui()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
