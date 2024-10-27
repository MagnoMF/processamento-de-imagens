import cv2
from matplotlib import pyplot as plt
from carregar_imagens import carregar_imagens_da_pasta
from verificar_pastas import verificar_ou_criar_pasta
import logger
import warnings
import time

def processar_imagens(imagens, pasta_img_processadas):
    for nome_arquivo, imagem in imagens:
        logger.log(f"Convertendo {nome_arquivo} para RGB")
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        canais = ('b', 'g', 'r')
        plt.figure(figsize=(8, 6))
        plt.subplot(1, 2, 1)
        for i, canal in enumerate(canais):
            histograma = cv2.calcHist([imagem], [i], None, [256], [0, 256])
            plt.plot(histograma, color=canal)
            plt.xlim([0, 256])
        plt.title('Histograma dos Canais de Cor')
        plt.xlabel('Intensidade de Pixels')
        plt.ylabel('Número de Pixels')
        
        plt.subplot(1, 2, 2)
        plt.imshow(imagem)
            
        plt.savefig(pasta_img_processadas+"histograma_"+nome_arquivo)
        logger.log(f"Imagem salva: {pasta_img_processadas}histograma_{nome_arquivo}")
        plt.show()
     
def run_histograma(pasta_img='../img', pasta_img_processadas = '../img_processadas/'):
    verificar_ou_criar_pasta(pasta_img)
    verificar_ou_criar_pasta(pasta_img_processadas)
    logger.log("Iniciando análise de histograma de imagens")
    inicio = time.perf_counter()
    imagens = carregar_imagens_da_pasta(pasta_img)
    processar_imagens(imagens, pasta_img_processadas)
    fim = time.perf_counter()
    logger.log(f"Imagens análisadas: {len(imagens)}")
    logger.log(f"Tempo de Execução: {fim-inicio:.2f}s")
    logger.log("Análise de histograma finalizada")

if __name__ == "__main__":
    run_histograma()