import cv2
from matplotlib import pyplot as plt
from carregar_imagens import carregar_imagens_da_pasta
from verificar_pastas import verificar_ou_criar_pasta
import logger
import warnings
import time

def aplicar_suavizacao(imagem):
    suavizacao_media = cv2.blur(imagem, (5, 5))
    suavizacao_gaussiana = cv2.GaussianBlur(imagem, (5, 5), 0)
    suavizacao_mediana = cv2.medianBlur(imagem, 5)

    return suavizacao_media, suavizacao_gaussiana, suavizacao_mediana

def processar_imagens(imagens, pasta_img_processadas):
    # Captura backend do matplotlib
    backend_plt = plt.get_backend()
    for nome_arquivo, imagem in imagens:
        suavizacao_media, suavizacao_gaussiana, suavizacao_mediana = aplicar_suavizacao(imagem)

        plt.figure(figsize=(12, 4))
        plt.subplot(1, 4, 1)
        plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
        plt.title('Original')
        plt.axis('off')

        plt.subplot(1, 4, 2)
        plt.imshow(cv2.cvtColor(suavizacao_media, cv2.COLOR_BGR2RGB))
        plt.title('Suavização Média')
        plt.axis('off')

        plt.subplot(1, 4, 3)
        plt.imshow(cv2.cvtColor(suavizacao_gaussiana, cv2.COLOR_BGR2RGB))
        plt.title('Suavização Gaussiana')
        plt.axis('off')

        plt.subplot(1, 4, 4)
        plt.imshow(cv2.cvtColor(suavizacao_mediana, cv2.COLOR_BGR2RGB))
        plt.title('Suavização Mediana')
        plt.axis('off')

        plt.suptitle(f"Técnicas de Suavização: {nome_arquivo}")
        plt.tight_layout()
        
        plt.savefig(pasta_img_processadas+"suavizacao_"+nome_arquivo)
        logger.log(f"Imagem salva: {pasta_img_processadas}suavizacao_{nome_arquivo}")
        
        # Tentar exibir imagem, se não conseguir manda apenas aviso
        try:
            with warnings.catch_warnings:
                plt.show()
        except Exception as e:
            logger.warn("Sistema não permite exibição de imagens")

def run_suavizacao(pasta_img='../img', pasta_img_processadas = '../img_processadas/'):
    verificar_ou_criar_pasta(pasta_img)
    verificar_ou_criar_pasta(pasta_img_processadas)
    logger.log("Iniciando suavização de imagens")
    inicio = time.perf_counter()
    imagens = carregar_imagens_da_pasta(pasta_img)
    processar_imagens(imagens, pasta_img_processadas)
    fim = time.perf_counter()
    logger.log(f"Imagens convertidas: {len(imagens)}")
    logger.log(f"Tempo de Execução: {fim-inicio:.2f}s")
    logger.log("Suavização finalizada")

if __name__ == "__main__":
    run_suavizacao()