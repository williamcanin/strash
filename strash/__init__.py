from pathlib import Path
from os.path import join

CONFIG = {
    "appname": ["sTrash", "strash"],  # Application/Script name
    "appversion": "0.2.0",  # Version script
    "pyversion": 3,  # Python version required
    "home": str(Path.home()),  # HOME user
    "trash_user": join(
        str(Path.home()), ".local/share/Trash/files/"
    ),  # Trash user system default
    "dep": ["find", "shred", "gio"],  # Dependencies
    "author1": {
        "name": "William C. Canin",
        "email": "william.costa.canin@gmail.com",
        "website": "https://williamcanin.github.io",
        "github": "https://github.com/williamcanin",
        "locale": "Brasil - SP",
    },
}
