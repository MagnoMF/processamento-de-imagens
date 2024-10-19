from datetime import datetime
import inspect

def log(mensagem, level=1): 
    """
    Level \n
    1: Info \n
    2: Warn
    """
    # Cores terminal
    RESET = "\033[0m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    
    # Captura nome do arquivo que chamou função de log
    frame_atual = inspect.currentframe().f_back
    nome_arquivo = frame_atual.f_code.co_filename
    
    # Formatando nome arquivo
    nome_arquivo = nome_arquivo.split('/')[-1].replace(".py", "")
    nome_arquivo = " ".join(word.capitalize() for word in nome_arquivo.split("_"))
    datetime_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if(level == 2):
        str=f"{YELLOW}{datetime_atual}    [{nome_arquivo}]{RESET} {mensagem}"
    else:
        str=f"{GREEN}{datetime_atual}    [{nome_arquivo}]{RESET} {mensagem}"
    print(str)