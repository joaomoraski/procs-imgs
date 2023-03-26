import numpy as np
import cv2

def knn(image, fx, fy):
    altura, largura = image.shape
    novaAltura = int(altura * fy)
    novaLargura = int(largura * fx)
    
    # Cria um array vazio para conter a imagem redimensionada
    imagemModificada = np.zeros((novaAltura, novaLargura), dtype=np.uint8)
    
    # Calcula o fator de escala para as direções x e y
    escalaX = largura / novaLargura
    escalaY = altura / novaAltura
    
    # Loop por cada pixel da nova imagem
    for i in range(novaAltura):
        for j in range(novaLargura):
            # Calcula aonde os pixels da imagem vao ficar na nova imagem
            x = int(j * escalaX)
            y = int(i * escalaY)
            
            # Seta o valor do pixel redimensionado para o valor do mais proximo vizinho da imagem original
            imagemModificada[i, j] = image[y, x]
    
    return imagemModificada

def  bilinearInterpolation(imagem, escalaX, escalaY):
    altura, largura = imagem.shape
    alturaNova = int(altura * escalaY)
    larguraNova = int(largura * escalaX)

    # cria a imagem ampliada/reduzida com zeros
    imagemAmpliadaReduzida = np.zeros((alturaNova, larguraNova), dtype=np.uint8)

    for yNovo in range(alturaNova):
        for xNovo in range(larguraNova):
            # encontra a posição correspondente na imagem original
            y = yNovo / escalaY
            x = xNovo / escalaX

            # verifica se a posição está dentro da imagem original
            if 0 <= y < altura - 1 and 0 <= x < largura - 1:
                # calcula as posições vizinhas
                i = int(y)
                j = int(x)
                a = imagem[i, j]
                b = imagem[i + 1, j]
                c = imagem[i, j + 1]
                d = imagem[i + 1, j + 1]

                # calcula as frações
                fy = y - i
                fx = x - j

                # interpola horizontalmente
                s1 = (1 - fx) * a + fx * c
                s2 = (1 - fx) * b + fx * d

                # interpola verticalmente
                valorInterpolado = int((1 - fy) * s1 + fy * s2)

                # define o valor na imagem ampliada/reduzida
                imagemAmpliadaReduzida[yNovo, xNovo] = valorInterpolado

    return imagemAmpliadaReduzida


def main():
    # Abre imagem e mostra a imagem original de inicio
    imgOriginal = cv2.imread('pratica2.jpg', cv2.IMREAD_COLOR)  # Abre a imagem em escala de cinza
    cv2.imshow('Imagem Original KNN', imgOriginal)  # Mostra a imagem na tela
    cv2.waitKey(0)  # Espera alguma tecla ser pressionada para continuar o código

    # Abre imagem e mostra ela apos ser reduzida
    imgReduzida = cv2.imread('pratica2.jpg', cv2.IMREAD_GRAYSCALE)  # Abre a imagem em escala de cinza
    novaImgReduzida = knn(imgReduzida, 0.5, 0.2)  # reduzir a imagem
    cv2.imshow('Imagem Reduzida KNN', novaImgReduzida)  # Mostra a imagem na tela
    cv2.waitKey(0)  # Espera alguma tecla ser pressionada para continuar o código
    cv2.imwrite('imagemReduzinaKNN.png', novaImgReduzida) # Escreve a imagem e um arquivo png

    # Abre imagem e mostra ela apos ser ampliada
    imgAmpliada = cv2.imread('pratica2.jpg', cv2.IMREAD_GRAYSCALE)  # Abre a imagem em escala de cinza
    novaImgAmpliada = knn(imgAmpliada, 5, 10)  # ampliar a imagem em fator de 10, 20
    cv2.imshow('Imagem Ampliada KNN', novaImgAmpliada)  # Mostra a imagem na tela
    cv2.waitKey(0)  # Espera alguma tecla ser pressionada para continuar o código
    cv2.destroyAllWindows() # fecha todas as janelas 
    cv2.imwrite('imagemAmpliadaKNN.png', novaImgAmpliada) # Escreve a imagem e um arquivo png


    # Abre imagem e mostra a imagem original de inicio
    # imgOriginal = cv2.imread('pratica2.jpg', cv2.IMREAD_COLOR)  # Abre a imagem em escala de cinza
    cv2.imshow('Imagem Original Bilinear', imgOriginal)  # Mostra a imagem na tela
    cv2.waitKey(0)  # Espera alguma tecla ser pressionada para continuar o código

    # Abre imagem e mostra ela apos ser reduzida
    # imgReduzida = cv2.imread('pratica2.jpg', cv2.IMREAD_GRAYSCALE)  # Abre a imagem em escala de cinza
    novaImgReduzida = bilinearInterpolation(imgReduzida, 0.5, 0.2)  # reduzir a imagem
    cv2.imshow('Imagem Reduzida Bilinear', novaImgReduzida)  # Mostra a imagem na tela
    cv2.waitKey(0)  # Espera alguma tecla ser pressionada para continuar o código
    cv2.imwrite('imagemReduzidaBilinear.png', novaImgReduzida) # Escreve a imagem e um arquivo png

    # Abre imagem e mostra ela apos ser ampliada
    # imgAmpliada = cv2.imread('pratica2.jpg', cv2.IMREAD_GRAYSCALE)  # Abre a imagem em escala de cinza
    novaImgAmpliada = bilinearInterpolation(imgAmpliada, 5, 10)  # ampliar a imagem em fator de 10, 20
    cv2.imshow('Imagem Ampliada Bilinear', novaImgAmpliada)  # Mostra a imagem na tela
    cv2.waitKey(0)  # Espera alguma tecla ser pressionada para continuar o código
    cv2.destroyAllWindows() # fecha todas as janelas 
    cv2.imwrite('imagemAmpliadaBilinear.png', novaImgAmpliada) # Escreve a imagem e um arquivo png


main()
