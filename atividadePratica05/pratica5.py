import cv2
import numpy as np

# Abre a imagem em escala de cinza
img = cv2.imread('pratica5_c.png', cv2.IMREAD_GRAYSCALE)

# Calcula o histograma manualmente
hist = np.zeros(256, dtype=int)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist[img[i,j]] += 1

# Calcula a distribuição de probabilidade acumulativa
cdf = np.cumsum(hist) / (img.shape[0]*img.shape[1])

# Calcula a transformação T(r)
T = np.uint8(255 * cdf)

# Aplica a transformação na imagem
img_equalizada = T[img]

# Exibe a imagem equalizada
cv2.imshow('Imagem Equalizada', img_equalizada)
cv2.waitKey(0)
cv2.destroyAllWindows()