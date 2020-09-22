from pathlib import Path
from os import makedirs

C_CONFIG_DIR = str(Path("~/.config/Inspyre-Softworks/mtgac.env").expanduser())

default_app_dir = str(Path('~/Inspyre-Softworks/MTGArena Companion').expanduser())

defaults = {
    'conf_dir': str(Path(default_app_dir + "/conf")),
    'data_dir': str(Path(default_app_dir + "/data"))
}

print(defaults)
print(C_CONFIG_DIR)

makedirs(defaults['data_dir'], exist_ok=True)
