import PySimpleGUIQt as GUI
from MTGArenaCompanion.lib.errors import ConfigAvailabilityError


def __get_conf_dir(default_path, critical):
    directory = GUI.PopupGetFolder('', default_path=default_path)
    if directory is None:
        raise ConfigAvailabilityError


def get_conf_dir(default_path, critical=True):
    try:
        __get_conf_dir(default_path, critical)
