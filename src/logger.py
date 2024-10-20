from datetime import datetime
import inspect
import os

def formatar_nome_arquivo(caminho_arquivo):
    nome_arquivo = os.path.basename(caminho_arquivo)
    nome_arquivo, _ = os.path.splitext(nome_arquivo)
    return nome_arquivo.replace("_", " ").replace("-", " ").title()

def data_hora():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def log(mensagem): 
    # Cores terminal
    RESET = "\033[0m"
    GREEN = "\033[32m"
    
    # Captura nome do arquivo que chamou função de log
    frame_atual = inspect.currentframe().f_back
    caminho_arquivo = frame_atual.f_code.co_filename
    
    # Formatando nome arquivo
    nome_arquivo = formatar_nome_arquivo(caminho_arquivo)
    
    print(f"{GREEN}{data_hora()}    [{nome_arquivo}]{RESET} {mensagem}")


def warn(mensagem):
    # Cores terminal
    RESET = "\033[0m"
    YELLOW = "\033[33m"
    
    # Captura nome do arquivo que chamou função de log
    frame_atual = inspect.currentframe().f_back
    caminho_arquivo = frame_atual.f_code.co_filename
    
    nome_arquivo = formatar_nome_arquivo(caminho_arquivo)
    print(f"{YELLOW}{data_hora()}    [{nome_arquivo}]{RESET} {mensagem}")