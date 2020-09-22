from pathlib import Path
from os import makedirs

C_CONFIG_DIR = str(Path("~/.config/Inspyre-Softworks/mtgac.env").expanduser())

defaults = {
    'data_dir': str(Path("~/Inspyre-Softworks/MTGArena Companion/data/test_folder").expanduser())
}

print(defaults)
print(C_CONFIG_DIR)

makedirs(defaults['data_dir'], exist_ok=True)
