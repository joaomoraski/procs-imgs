import cv2
import numpy as np
import matplotlib.pyplot as plt

def piecewiseLinear(img, r1, s1, r2, s2):
    # Verifica se a imagem é de ponto flutuante e a normaliza para [0, 255]
    if img.dtype == np.float32 or img.dtype == np.float64:
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Aplica a transformação piecewise-linear
    # Pega o tamanho e altura da imagem
    height, width = img.shape[:2]
    # Cria um array para armazenar a imagem transformada
    imgTransformed = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            # for pela imagem para fazer as operações do transformação
            if img[i, j] < r1:
                imgTransformed[i, j] = s1 * img[i, j] / r1
            elif img[i, j] < r2:
                imgTransformed[i, j] = ((s2 - s1) / (r2 - r1)) * (img[i, j] - r1) + s1
            else:
                imgTransformed[i, j] = ((255 - s2) / (255 - r2)) * (img[i, j] - r2) + s2

    return imgTransformed


def main():
    # Carrega a imagem de teste
    img = cv2.imread("pratica4.png", cv2.IMREAD_GRAYSCALE)

    # Exibe a imagem de entrada
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Imagem de entrada")

    # Aplica a transformação piecewise-linear para ajustar o contraste
    imgTransformed = img
    entrada01 = [0, 69, 185 , 255]
    entrada02 = [0, 124, 161, 255]
    imgTransformed = piecewiseLinear(img, 100, 50, 200, 200)
    cv2.imwrite("imagem_transformada.png", imgTransformed)

    # Exibe a imagem transformada
    plt.subplot(1, 2, 2)
    plt.imshow(imgTransformed, cmap="gray")
    plt.title("Imagem transformada")

    plt.show()

main()