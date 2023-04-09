import cv2
import numpy as np

def componentesConexasRecursiva(i, j, rotuloAtual, imgBinarizada, imgRotulada):
    # Percorre os pixels da imagem binaria e rotula os componentes conexos
    # 0 representa o fundo e diferente de 0 representa diferentes componentes
    linhasAdj = [-1, -1, -1, 0, 0, 1, 1, 1]
    colunasAdj = [-1, 0, 1, -1, 1, -1, 0, 1]

    imgRotulada[i,j] = rotuloAtual

    for k in range(len(linhasAdj)):
        linhas = i + linhasAdj[k]
        colunas = j + colunasAdj[k]
        if linhas > 0 and linhas <= imgBinarizada.shape[0] and colunas > 0 and colunas <= imgBinarizada.shape[1]:
            if imgBinarizada[linhas, colunas] and imgRotulada[linhas, colunas] == 0:
                imgRotulada = componentesConexasRecursiva(linhas, colunas, rotuloAtual, imgBinarizada, imgRotulada)

    return imgRotulada

def main():
    # A imagem precisou ser transformada me png pois o python n aceita abrir uma imagem em gif
    img = cv2.imread('pratica3_tur.png', cv2.IMREAD_GRAYSCALE) # Abre a imagem em escala de cinza 

    limite = 44  # Define um limite
    imgBinarizada = img < limite

    # Binarizar a imagem usando um limite adequado
    se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20)) # Aumenta o tamanho dos pixels rotulados para conectar as regiões
    imgBinarizadaFechada = cv2.morphologyEx(imgBinarizada.astype(np.uint8), cv2.MORPH_CLOSE, se) # Aplica uma operação de fechamento para conectar regiões

    nrows, ncols = imgBinarizadaFechada.shape # Cria matriz para rotular
    imgRotulada = np.zeros((nrows, ncols), dtype=np.uint8)
    rotuloAtual = 0

    for i in range(nrows):
        for j in range(ncols):
            if imgBinarizadaFechada[i,j] and imgRotulada[i,j] == 0:
                rotuloAtual += 1
                imgRotulada = componentesConexasRecursiva(i, j, rotuloAtual, imgBinarizadaFechada, imgRotulada)

    numPerus = rotuloAtual
    print(f"Foram encontrados {numPerus} perus na imagem.")

    cv2.imshow('Imagem Rotulada', imgRotulada*255)
    cv2.imwrite('imagemRotulada_perus.png', imgRotulada*255)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
