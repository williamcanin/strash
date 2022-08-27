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
    "dep": ("find", "shred", "gio"),  # Dependencies
    "author1": {
        "name": "William C. Canin",
        "email": "william.costa.canin@gmail.com",
        "website": "https://williamcanin.github.io",
        "github": "https://github.com/williamcanin",
        "locale": "Brasil - SP",
    },
}


LANG = {
    "en_US": {},
    "pt_BR": {
        "done": ">>> Concluído!",
        "str1": ">>> Iniciando a remoção segura...",
        "str2": "Confirmação",
        "str3": (
            "Desejar excluir permanentemente o(s) arquivo(s) de forma SEGURA?\n"
            "ATENÇÃO!!! ESTÁ AÇÃO É IRREVESSÍVEL!"
        ),
        "str4": ">>> ERRO: Caminho de diretório ou caminho de arquivo incorreto.",
        "str5": ">>> Limpando a lixeira com segurança...",
        "str6": ">>> Trash is already empty. :)",
        "str7": f"Ocorreu um erro inesperado que {CONFIG['appname'][0]} não consegue identificar.",
        "str8": f"{CONFIG['appname'][0]} não tem permissão para executar as tarefas.",
        "str9": f"{CONFIG['appname'][1]} [opções]",
    },
}
