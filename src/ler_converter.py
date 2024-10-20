import cv2
import os
import time
from carregar_imagens import carregar_imagens_da_pasta
from verificar_pastas import verificar_ou_criar_pasta
import logger
import warnings
from matplotlib import pyplot as plt

def exibir_imagens(imagens, pasta_img_processadas):
    # Captura backend do matplotlib
    backend_plt = plt.get_backend()
    
    for nome_arquivo, imagem in imagens:
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        plt.figure(figsize=(10, 4))

        plt.subplot(1, 4, 1)
        plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
        plt.title('Original')
        plt.axis('off')

        plt.subplot(1, 4, 2)
        plt.imshow(imagem_rgb)
        plt.title('RGB')
        plt.axis('off')

        plt.subplot(1, 4, 3)
        plt.imshow(imagem_hsv)
        plt.title('HSV')
        plt.axis('off')

        plt.subplot(1, 4, 4)
        plt.imshow(imagem_cinza, cmap='gray')
        plt.title('Cinza')
        plt.axis('off')

        plt.suptitle(f"Transformações da imagem: {nome_arquivo}")
        plt.tight_layout()
        plt.savefig(pasta_img_processadas+"conversao_"+nome_arquivo)
        logger.log(f"Imagem salva: {pasta_img_processadas}conversao_{nome_arquivo}")
        
        # Tentar exibir imagem, se não conseguir manda apenas aviso
        try:
            with warnings.catch_warnings:
                plt.show()
        except Exception as e:
            logger.warn("Sistema não permite exibição de imagens")


def run_conversor(pasta_img='../img', pasta_img_processadas = '../img_processadas/'):
    verificar_ou_criar_pasta(pasta_img)
    verificar_ou_criar_pasta(pasta_img_processadas)
    logger.log("Iniciando Leitura e conversão de imagens")
    inicio = time.perf_counter()
    imagens = carregar_imagens_da_pasta(pasta_img)
    exibir_imagens(imagens, pasta_img_processadas)
    fim = time.perf_counter()
    logger.log(f"Imagens convertidas: {len(imagens)}")
    logger.log(f"Tempo de Execução: {fim-inicio:.2f}s")
    logger.log("Leitura e conversão finalizada")
    
if __name__ == "__main__":
    run_conversor()