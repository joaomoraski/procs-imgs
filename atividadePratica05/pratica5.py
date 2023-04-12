import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    imagens = ["pratica5.png", "pratica5_c.png"]
    print("0 - pratica5.png\n1 - pratica5_c.png")
    opcao = int(input("Seleciona a imagem a ser utilizada: "))
    if opcao > 1 or opcao < 0:
        print("Trolla nao, escolhe certo ai pfv")
        return
        
    # Abre a imagem em escala de cinza
    img = cv2.imread(imagens[opcao], cv2.IMREAD_GRAYSCALE)

    # Calcula o histograma manualmente
    hist = np.zeros(256, dtype=int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist[img[i,j]] += 1

    # Cálculo da distribuição de probabilidade
    pdf = hist / np.sum(hist)

    # Cálculo da distribuição acumulada
    cdf = np.zeros(256)
    cumulativeSum = 0
    for i in range(len(pdf)):
        cumulativeSum += pdf[i]
        cdf[i] = cumulativeSum

    # Calcula a transformação T(r)
    T = np.uint8(255 * cdf)

    # Aplica a transformação na imagem
    imgEqualizada = T[img]

    # Calcula o histograma da imagem equalizada
    histEqualizado = np.zeros(256, dtype=int)
    for i in range(imgEqualizada.shape[0]):
        for j in range(imgEqualizada.shape[1]):
            histEqualizado[imgEqualizada[i,j]] += 1

    # Plota o histograma das imagens original e equalizada
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
    ax[0][0].plot(hist)
    ax[0][0].set_title('Histograma da imagem original')
    ax[0][1].plot(histEqualizado)
    ax[0][1].set_title('Histograma da imagem equalizada')
    ax[1][0].plot(T)
    ax[1][0].set_title('Função T(r)')
    ax[1][1].imshow(cv2.cvtColor(imgEqualizada, cv2.IMREAD_GRAYSCALE))
    ax[1][1].set_title('Imagem Equalizada')
    plt.show()

main()