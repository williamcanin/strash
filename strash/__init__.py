from pathlib import Path
from os.path import join
from datetime import date
from sys import version_info

CONFIG = {
    "appname": ["sTrash", "strash"],  # Application/Script name
    "appversion": "0.2.0",  # Version script
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
        "str11": f"{CONFIG['appname'][0]} © 2018-{date.today().year} - All rights reserved.",
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
        "ApproachedUser": f'{CONFIG["appname"][0]} não pode ser executado com superusuário (root) com ID 0. Abortado!',
        "IncompatibleVersion": (
            f'{CONFIG["appname"][0]} requer a versão {CONFIG["pyversion"]} do Python. '
            f"Você está usando a version {version_info[0]}."
        ),
        "AbsentDependency": "A seguinte dependências está ausente: ",
        "InvalidOS": f'{CONFIG["appname"][0]} é compatível apenas com sistemas "posix". Seu sistema é: ',
        "done": ">>> Concluído!",
        "str1": ">>> Iniciando a remoção segura...",
        "str2": "Confirmação",
        "str3": (
            "Desejar excluir permanentemente o(s) arquivo(s) de forma SEGURA?\n"
            'ATENÇÃO!!! ESTÁ AÇÃO É IRREVERSÍVEL SE VOCÊ CLICAR EM "SIM"!'
        ),
        "str4": ">>> ERRO: Caminho de diretório ou caminho de arquivo incorreto.",
        "str5": ">>> Limpando a lixeira com segurança...",
        "str6": ">>> Lixeira já está vazia. :)",
        "str7": f"Ocorreu um erro inesperado que {CONFIG['appname'][0]} não consegue identificar.",
        "str8": f"{CONFIG['appname'][0]} não tem permissão para executar as tarefas.",
        "str9": f"{CONFIG['appname'][1]} [opções]",
        "str10": (
            f'O {CONFIG["appname"][0]} é um programa que roda em cima do "shred" para limpar as '
            f"lixeiras e arquivos com segurança sem deixar rastros."
        ),
        "str11": f"{CONFIG['appname'][0]} © 2018-{date.today().year} - Todos os direitos reservados.",
        "str12": "remove uma pasta ou arquivo especificado (recursivo para pastas)",
        "str13": "não mostre a caixa de diálogo para confirmação da ação. (Apenas para a opção --path)",
        "str14": "substitui N vezes em vez de 3, o padrão",
        "str15": "remova e feche com segurança o terminal (somente para terminal)",
        "str16": "mostrar os créditos",
        "str17": ">>> Erro ao passar argumentos",
        "str18": "Versão",
        "str19": "Créditos",
        "str20": "Autor",
        "str21": "Página pessoal",
        "str22": "País",
        "str23": "Obrigado dependências",
        "str24": "Página do projeto",
        "str25": "mostrar versão",
    },
}
