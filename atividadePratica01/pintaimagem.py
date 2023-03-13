import numpy as np
import cv2

def main():
    # Cria uma matriz de 100x100 com 3 canais de cores
    img = np.random.rand(100, 100, 3)

    # Multiplica cada pixel da imagem por 255 para garantir que a intensidade esteja no intervalo correto (0 a 255)
    img = img * 255

    img[19,:,:] = 0;
    img[:,40,:] = 255;

    img[19,0:14,0] = 0 # blue
    img[19,0:14,1] = 0 # green
    img[19,0:14,2] = 255 # red

    # Converte a matriz para o tipo de dados uint8 (números inteiros de 0 a 255)
    img = img.astype(np.uint8)

    img_resized = cv2.resize(img, (800, 600), interpolation=cv2.INTER_LINEAR)
    # Exibe a imagem em uma janela chamada "Imagem"
    cv2.imshow('Imagem', img_resized)

    # Aguarda uma tecla ser pressionada para fechar a janela
    cv2.waitKey(0)

    # Fecha todas as janelas abertas pelo OpenCV
    cv2.destroyAllWindows()
    return


main()
