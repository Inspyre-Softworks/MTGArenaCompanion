

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

    def inspect_self(self):
        print(dir(self))