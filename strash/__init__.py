from pathlib import Path
from os.path import join
from datetime import date
from sys import version_info

CONFIG = {
    "appname": ["sTrash", "strash"],  # Application/Script name
    "appversion": "0.2.0",  # Version script
    "pyversion": 4,  # Python version required
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
        "ApproachedUser": f'{CONFIG["appname"][0]} não pode ser executado com superusuário (root) com ID 0. Abortado!',
        "IncompatibleVersion": (
            f'{CONFIG["appname"][0]} requer a versão {CONFIG["pyversion"]} do Python. '
            f"Você está usando a version {version_info[0]}."
        ),
        "AbsentDependency": "A seguinte dependências está ausente: ",
        "done": ">>> Concluído!",
        "str1": ">>> Iniciando a remoção segura...",
        "str2": "Confirmação",
        "str3": (
            "Desejar excluir permanentemente o(s) arquivo(s) de forma SEGURA?\n"
            'ATENÇÃO!!! ESTÁ AÇÃO É IRREVESSÍVEL SE VOCÊ CLICAR EM "SIM"!'
        ),
        "str4": ">>> ERRO: Caminho de diretório ou caminho de arquivo incorreto.",
        "str5": ">>> Limpando a lixeira com segurança...",
        "str6": ">>> Trash is already empty. :)",
        "str7": f"Ocorreu um erro inesperado que {CONFIG['appname'][0]} não consegue identificar.",
        "str8": f"{CONFIG['appname'][0]} não tem permissão para executar as tarefas.",
        "str9": f"{CONFIG['appname'][1]} [opções]",
        "str10": (
            f'O {CONFIG["appname"][0]} é um programa que roda em cima do "shred" para limpar as '
            f"lixeiras e arquivos com segurança sem deixar rastros."
        ),
        "str11": f"{CONFIG['appname'][0]} © 2018-{date.today().year} - Todos os direitos reservados.",
        "str12": "remove uma pasta ou arquivo especificado (recursivo)",
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
    },
}
