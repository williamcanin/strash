from pathlib import Path
from os.path import join
from datetime import date
from sys import version_info

CONFIG = {
    "appname": ["sTrash", "strash"],  # Application/Script name
    "appversion": "0.2.0",  # Version script
    "url": "http://github.com/williamcanin/strash",
    "pyversion": 3,  # Python version required
    "home": str(Path.home()),  # HOME user
    "trash_user": join(
        str(Path.home()), ".local/share/Trash/files/"
    ),  # Trash user system default
    "dep": ("shred", "gio"),  # Dependencies
    "author1": {
        "name": "William C. Canin",
        "email": "william.costa.canin@gmail.com",
        "website": "https://williamcanin.github.io",
        "github": "https://github.com/williamcanin",
        "locale": "Brasil - SP",
    },
}


LANG = {
    "en_US": {
        "ApproachedUser": f'{CONFIG["appname"][0]} cannot be run with superuser (root) with ID 0. Aborted!',
        "IncompatibleVersion": (
            f'{CONFIG["appname"][0]} requires the {CONFIG["pyversion"]} version of Python. '
            f"You are using version {version_info[0]}."
        ),
        "AbsentDependency": "The following dependencies are missing: ",
        "InvalidOS": f'{CONFIG["appname"][0]} is only compatible with "posix" systems. Your system is: ',
        "done": ">>> Done!",
        "str1": ">>> Starting safe removal...",
        "str2": "Confirmation",
        "str3": (
            "Want to permanently delete the file(s) SECURELY?\n"
            'WARNING!!! THIS ACTION IS IRREVERSIBLE IF YOU CLICK "YES"!'
        ),
        "str4": ">>> ERROR: Incorrect directory path or file path.",
        "str5": ">>> Safely cleaning the recycle bin...",
        "str6": ">>> Trash is already empty. :)",
        "str7": f"An unexpected error occurred that {CONFIG['appname'][0]} cannot identify.",
        "str8": f"{CONFIG['appname'][0]} does not have permission to run the tasks.",
        "str9": f"{CONFIG['appname'][1]} [options]",
        "str10": (
            f'{CONFIG["appname"][0]} is a program that runs on top of "shred" to clean the '
            f"recycle bins and files safely without leaving a trace."
        ),
        "str11": f"{CONFIG['appname'][0]} ?? 2018-{date.today().year} - All rights reserved.",
        "str12": "remove a specified folder or file (recursive for folders)",
        "str13": "do not show the action confirmation dialog. (For --path option only)",
        "str14": "replaces N times instead of 3, the default",
        "str15": "safely remove and close the terminal (terminal only)",
        "str16": "show credits",
        "str17": ">>> Error passing arguments",
        "str18": "Version",
        "str19": "Credits",
        "str20": "Author",
        "str21": "Personal page",
        "str22": "Country",
        "str23": "Thank you dependencies",
        "str24": "Project page",
        "str25": "show version",
    },
    "pt_BR": {
        "ApproachedUser": f'{CONFIG["appname"][0]} n??o pode ser executado com superusu??rio (root) com ID 0. Abortado!',
        "IncompatibleVersion": (
            f'{CONFIG["appname"][0]} requer a vers??o {CONFIG["pyversion"]} do Python. '
            f"Voc?? est?? usando a version {version_info[0]}."
        ),
        "AbsentDependency": "A seguinte depend??ncias est?? ausente: ",
        "InvalidOS": f'{CONFIG["appname"][0]} ?? compat??vel apenas com sistemas "posix". Seu sistema ??: ',
        "done": ">>> Conclu??do!",
        "str1": ">>> Iniciando a remo????o segura...",
        "str2": "Confirma????o",
        "str3": (
            "Desejar excluir permanentemente o(s) arquivo(s) de forma SEGURA?\n"
            'ATEN????O!!! EST?? A????O ?? IRREVERS??VEL SE VOC?? CLICAR EM "SIM"!'
        ),
        "str4": ">>> ERRO: Caminho de diret??rio ou caminho de arquivo incorreto.",
        "str5": ">>> Limpando a lixeira com seguran??a...",
        "str6": ">>> Lixeira j?? est?? vazia. :)",
        "str7": f"Ocorreu um erro inesperado que {CONFIG['appname'][0]} n??o consegue identificar.",
        "str8": f"{CONFIG['appname'][0]} n??o tem permiss??o para executar as tarefas.",
        "str9": f"{CONFIG['appname'][1]} [op????es]",
        "str10": (
            f'O {CONFIG["appname"][0]} ?? um programa que roda em cima do "shred" para limpar as '
            f"lixeiras e arquivos com seguran??a sem deixar rastros."
        ),
        "str11": f"{CONFIG['appname'][0]} ?? 2018-{date.today().year} - Todos os direitos reservados.",
        "str12": "remove uma pasta ou arquivo especificado (recursivo para pastas)",
        "str13": "n??o mostre a caixa de di??logo para confirma????o da a????o. (Apenas para a op????o --path)",
        "str14": "substitui N vezes em vez de 3, o padr??o",
        "str15": "remova e feche com seguran??a o terminal (somente para terminal)",
        "str16": "mostrar os cr??ditos",
        "str17": ">>> Erro ao passar argumentos",
        "str18": "Vers??o",
        "str19": "Cr??ditos",
        "str20": "Autor",
        "str21": "P??gina pessoal",
        "str22": "Pa??s",
        "str23": "Obrigado depend??ncias",
        "str24": "P??gina do projeto",
        "str25": "mostrar vers??o",
    },
}
