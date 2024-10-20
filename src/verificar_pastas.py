import os
import logger

def verificar_ou_criar_pasta(pasta):
    if not os.path.exists(pasta):
        try:
            os.makedirs(pasta)  # Cria a pasta
            logger.log(f"A pasta '{pasta}' foi criada.")
        except Exception as e:
            logger.log(f"Ocorreu um erro ao criar a pasta: {e}")
    else:
        logger.warn(f"A pasta '{pasta}' já existe.")