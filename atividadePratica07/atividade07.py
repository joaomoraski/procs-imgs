import cv2
import numpy as np
import matplotlib.pyplot as plt


# Passo 1 - Carregar a imagem
img = cv2.imread('pratica7.png')

# Passo 2 - Criar filtro de média 5x5
filtro = np.ones((5, 5), dtype=np.float32) / 25

# Passo 3 - Aplicar o filtro na imagem
imgFiltrada1 = cv2.filter2D(img, -1, filtro)

# Criar a imagem com bordas adicionadas
mpad = cv2.copyMakeBorder(img, 4, 4, 4, 4, cv2.BORDER_REFLECT)

# Criar o filtro gaussiano 9x9
f_gauss = cv2.getGaussianKernel(9, 2)
f_gauss = f_gauss * f_gauss.T

# Aplicar o filtro gaussiano na imagem com bordas adicionadas
gauss_m = cv2.filter2D(mpad, -1, f_gauss)

# Cortar as bordas adicionadas da imagem filtrada
gauss_m = gauss_m[4:-4, 4:-4]

# Utilizar a função cv2.filter2D() para aplicar o filtro de média e o filtro gaussiano
imgFiltrada2 = cv2.filter2D(img, -1, filtro)
imgFiltrada3 = cv2.filter2D(img, -1, f_gauss)

# Salvar as imagens
cv2.imwrite('imgFiltrada1.png', imgFiltrada1)
cv2.imwrite('imgFiltrada2.png', imgFiltrada2)
cv2.imwrite('imgFiltrada3.png', imgFiltrada3)
cv2.imwrite('gauss_m.png', gauss_m)

#  Plota o histograma das imagens original e filtrada
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
ax[0][0].imshow(imgFiltrada1)
ax[0][0].set_title('Imagem filtrada média 5x5')
ax[0][1].imshow(imgFiltrada2)
ax[0][1].set_title('Imagem filtrada Gauss 9x9')
ax[1][0].imshow(imgFiltrada3)
ax[1][0].set_title('Imagem filtrada média 5x5 imfilter')
ax[1][1].imshow(gauss_m)
ax[1][1].set_title('Imagem filtrada Gauss 9x9 imfilter')
plt.show()
