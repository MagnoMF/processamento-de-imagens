import os
import cv2
import logger

def carregar_imagens_da_pasta(caminho_pasta):
    imagens = []
    arquivos = os.listdir(caminho_pasta)
    if(not len(arquivos)):
        logger.log("Pasta de imagens está vazia")
        raise Exception(f"A pasta de imagens está vazia")

    for nome_arquivo in arquivos:
        caminho_imagem = os.path.join(caminho_pasta, nome_arquivo)
        imagem = cv2.imread(caminho_imagem)
        if imagem is not None:
            imagens.append((nome_arquivo, imagem))
    return imagens