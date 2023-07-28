import cv2
import numpy as np


def calcular_diferenca(img1, img2):
    # Converte as imagens para float32
    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)
    # Calcula a diferença entre as imagens
    diff = cv2.absdiff(img1, img2)
    # Soma as diferenças em cada canal da imagem
    diff = np.sum(diff, axis=2)
    # Calcula a média das diferenças
    diffMean = np.mean(diff)
    return diffMean


def main():
    # Carrega a imagem
    img = cv2.imread('pratica6.png')
    # Cria o ruído gaussiano com média zero e variância 64
    noise = np.random.normal(0, 64, img.shape)
    # Adiciona o ruído à imagem
    imgNoise = img.astype(np.float64) + noise
    # Normaliza os valores para o intervalo [0, 255]
    cv2.normalize(imgNoise, imgNoise, 0, 255, cv2.NORM_MINMAX)
    imgNoise = imgNoise.astype(np.uint8)
    # Mostra os histogramas
    cv2.imshow('Original', img)
    cv2.imshow('Com Ruido', imgNoise)
    # Calcula e mostra o histograma da imagem original
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    cv2.imshow('Histograma Original', hist)
    # Calcula e mostra o histograma da imagem com ruído
    histNoise = cv2.calcHist([imgNoise], [0], None, [256], [0, 256])
    cv2.imshow('Histograma Com Ruído', histNoise)
    # Mostra as imagens e aguarda uma tecla ser pressionada
    cv2.waitKey(0)
    # Calcula a diferença entre as imagens
    diff = calcular_diferenca(img, imgNoise)
    # Imprime o resultado
    print('Diferença entre as imagens:', diff)


main()