import cv2
import time
from verificar_pastas import verificar_ou_criar_pasta
from carregar_imagens import carregar_imagens_da_pasta
import logger
from matplotlib import pyplot as plt

def detectar_faces(imagens, pasta_img_processadas):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    for imagem in imagens:
        scaleFactor = 1.05
        faces = face_cascade.detectMultiScale(imagem[1], scaleFactor, minNeighbors=5, minSize=(30, 30))
        if(len(faces)):
            logger.log(f"Em {imagem[0]} foram detectados {len(faces)} rostos")
            for (x, y, w, h) in faces:
                cv2.rectangle(imagem[1], (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_gray = imagem[1][y:y + h, x:x + w]
                roi_color = imagem[1][y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
            cv2.imwrite(f"{pasta_img_processadas}/faces_{imagem[0]}", imagem[1])
            plt.imshow(imagem[1])
            plt.show()
        else:
            logger.warn(f"Em {imagem[0]} nenhuma face foi detectada")
    

def run_deteccao_faces(pasta_img='../img', pasta_img_processadas = '../img_processadas/'):
    verificar_ou_criar_pasta(pasta_img)
    verificar_ou_criar_pasta(pasta_img_processadas)
    logger.log("Iniciando Leitura e detecção de rostos")
    inicio = time.perf_counter()
    imagens = carregar_imagens_da_pasta(pasta_img)
    detectar_faces(imagens, pasta_img_processadas)
    fim = time.perf_counter()
    logger.log(f"Imagens processadas: {len(imagens)}")
    logger.log(f"Tempo de Execução: {fim-inicio:.2f}s")
    logger.log("Leitura e detecção finalizada")


if __name__ == "__main__":
    run_deteccao_faces()