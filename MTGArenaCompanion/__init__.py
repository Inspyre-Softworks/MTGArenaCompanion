from configparser import ConfigParser
import PySimpleGUIQt as Qt
from os import makedirs
from pathlib import Path

DEFAULT_DATA_DIR = str(
    Path("~/Inspyre-Softworks/MTGA-Companion/data").expanduser())


gh_issue_base_url = 'https://github.com/Inspyre-Softworks/MTG-Arena-Companion/issues/new?'
gh_issue_bug_labels = 'labels=Bug::Unconfirmed'
gh_issue_bug_assignee = '&assignee=tayjaybabee'
gh_issue_bug_prefix = '&title=[Bug%20Report]'
gh_bug_report_url = str(gh_issue_base_url + gh_issue_bug_labels +
                        gh_issue_bug_assignee + gh_issue_bug_prefix)
print(gh_bug_report_url)


class MTGACApp(object):

    runtime_args = None
    # from MTGArenaCompanion.GUI.windows.start import StartWindow
    # from MTGArenaCompanion.lib.arg_parse import ArgParser

    start_window = None
    log_device = None

    def __default_cache__(self):
        _ = {
            'app_plist': {
                'version': 'development(1.0)',
                'install_date': None,
                'last_update': None,
                'updates_since_cached': 0,
            },

            'app_data': {
                'conf_dir': self.defaults['conf_dir'],
            },
        }

        return _

    def __init__(self):
        from MTGArenaCompanion.lib import C_CONFIG_DIR, Path, defaults
        self.defaults = defaults
        parser = ConfigParser()
        print('Initializing')
        print(C_CONFIG_DIR)

        new_directory = None

        if Path(C_CONFIG_DIR).exists():
            parser.read(C_CONFIG_DIR)
            self.conf_file = str(parser.get(
                'APP_CONF', 'data_directory')) + "/conf.ini"
            print(self.conf_file)

        else:
            print(self.__default_cache__())
            cache = self.__default_cache__()
            directory = Qt.PopupGetFolder(
                '', default_path=cache['app_data']['conf_dir'])
            makedirs(directory, exist_ok=True)
            print(directory)
            new_directory = str(Path(directory).expanduser().resolve())

        ccd_list = C_CONFIG_DIR.split('/')
        ccd_list.pop(-1)
        ccd = '/'.join(ccd_list)

        makedirs(ccd, exist_ok=True)

        if new_directory:
            parser.add_section('APP_CONF')
            parser.set('APP_CONF', 'data_directory', new_directory)

            with open(C_CONFIG_DIR, 'w+') as env_file:
                parser.write(env_file)

    def inspect_self(self):
        print(dir(self))
