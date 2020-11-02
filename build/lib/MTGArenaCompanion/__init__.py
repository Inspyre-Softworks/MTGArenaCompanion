from configparser import ConfigParser
import PySimpleGUIQt as Qt

gh_issue_base_url = 'https://github.com/Inspyre-Softworks/MTG-Arena-Companion/issues/new?'
gh_issue_bug_labels = 'labels=Bug::Unconfirmed'
gh_issue_bug_assignee = '&assignee=tayjaybabee'
gh_issue_bug_prefix= '&title=[Bug%20Report]'
gh_bug_report_url = str(gh_issue_base_url + gh_issue_bug_labels + gh_issue_bug_assignee + gh_issue_bug_prefix)
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
        if Path(C_CONFIG_DIR).exists():
            self.conf_cache = parser.read(C_CONFIG_DIR)
            conf_file = self.conf_cache['conf_file']
        else:
            print(self.__default_cache__())
            cache = self.__default_cache__()
            Qt.PopupGetFolder('', default_path=cache['app_data']['conf_dir'])



    def inspect_self(self):
        print(dir(self))