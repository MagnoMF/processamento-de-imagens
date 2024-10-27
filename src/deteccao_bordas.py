import cv2
import time
from verificar_pastas import verificar_ou_criar_pasta
from carregar_imagens import carregar_imagens_da_pasta
import logger
import warnings
from matplotlib import pyplot as plt


def aplicar_detectores_de_borda(imagem):
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    bordas_canny = cv2.Canny(imagem_cinza, 100, 200)
    
    borda_sobelx = cv2.Sobel(imagem_cinza, cv2.CV_64F, 1, 0, ksize=5)
    borda_sobely = cv2.Sobel(imagem_cinza, cv2.CV_64F, 0, 1, ksize=5)
    bordas_sobel = cv2.magnitude(borda_sobelx, borda_sobely)

    return bordas_canny, bordas_sobel

def processar_imagens(imagens, pasta_img_processadas):
    for nome_arquivo, imagem in imagens:
        bordas_canny, bordas_sobel = aplicar_detectores_de_borda(imagem)

        plt.figure(figsize=(12, 4))
        plt.subplot(1, 3, 1)
        plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
        plt.title('Original')
        plt.axis('off')

        plt.subplot(1, 3, 2)
        plt.imshow(bordas_canny, cmap='gray')
        plt.title('Bordas - Canny')
        plt.axis('off')

        plt.subplot(1, 3, 3)
        plt.imshow(bordas_sobel, cmap='gray')
        plt.title('Bordas - Sobel')
        plt.axis('off')

        plt.suptitle(f"Detecção de Bordas: {nome_arquivo}")
        plt.tight_layout()
        
        plt.savefig(pasta_img_processadas+"deteccao_bordas_"+nome_arquivo)
        logger.log(f"Imagem salva: {pasta_img_processadas}deteccao_bordas_{nome_arquivo}")
        plt.show()


def run_deteccao(pasta_img='../img', pasta_img_processadas = '../img_processadas/'):
    verificar_ou_criar_pasta(pasta_img)
    verificar_ou_criar_pasta(pasta_img_processadas)
    logger.log("Iniciando Leitura e conversão de imagens")
    inicio = time.perf_counter()
    imagens = carregar_imagens_da_pasta(pasta_img)
    processar_imagens(imagens, pasta_img_processadas)
    fim = time.perf_counter()
    logger.log(f"Imagens convertidas: {len(imagens)}")
    logger.log(f"Tempo de Execução: {fim-inicio:.2f}s")
    logger.log("Leitura e conversão finalizada")

if __name__ == "__main__":
    run_deteccao()