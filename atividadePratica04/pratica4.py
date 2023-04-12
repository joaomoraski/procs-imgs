import cv2
import numpy as np
import matplotlib.pyplot as plt

def piecewiseLinear(img, r, s):
    # Armazena dimensões da imagem de entrada 
    linhas, colunas, canais = img.shape
    # Inicializa a matriz com as mesmas dimensões da imagem de entrada
    imgSaida = np.zeros((linhas, colunas, canais), dtype=np.uint8)
    for linha in range(linhas):
        for coluna in range(colunas):
            for canal in range(canais):
                # Obtém o pixel e transforma em float para evitar erros de arredondamento
                pixel = float(img[linha, coluna, canal])
                if pixel <= r[0]:
                    imgSaida[linha, coluna, canal] = s[0] # Se for menor ou igual ao valor mínimo ,o valor será o valor mínimo
                elif pixel >= r[-1]:
                    imgSaida[linha, coluna, canal] = s[-1] # Se for maior ou igual ao valor maximo, o valor será o valor máximo
                else: # Senão, percorre os intervalos
                    for i in range(len(r)-1):
                        # Se estiver no intervalo atual, utiliza a formula e calcula o valor para o píxel.
                        if pixel >= r[i] and pixel <= r[i+1]:
                            imgSaida[linha, coluna, canal] = int(((s[i+1]-s[i])/(r[i+1]-r[i])) * (pixel - r[i]) + s[i])
                            break
    return imgSaida



def main():
    # Carrega a imagem de teste
    img = cv2.imread("pratica4.png")

    # Criando uma lista de arrays que vai ser os valores de teste
    entradasR = [[0, 69, 185 , 255], [69, 69, 200, 255], [25, 125,200,140], [198,248,95,195]]
    entradasS = [[0, 124, 161, 255], [0,161,124,255], [20,15,88,99], [220,188,177,222]]
    # Cria o subplot das imagens para apresentar na tela
    fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(10, 10))
    # Define como fullscreen padrao
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    # Aumenta o espaçamento das imagens
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    # Preenche a imagem original para todas as linhas de todos os casos de teste
    for i in range(4):
        ax[i][0].imshow(img)
        ax[i][0].set_title('Imagem original')
    # Faz a logica do piecewise em 4 imagens diferentes e preenche elas na segunda coluna de cada linha com o titulo mostrando o caso de teste
    for i in range(len(entradasR)):    
        # Aplica a transformação piecewise-linear para ajustar o contraste
        imgTransformed = piecewiseLinear(img, entradasR[i], entradasS[i])
        cv2.imwrite("imagemTransformada"  + str(i+1) + ".png", imgTransformed)
        ax[i][1].imshow(imgTransformed)
        ax[i][1].set_title('Imagem transformada usando ' + str(entradasR[i]) + " " + str(entradasS[i]))

    # Exibe as imagens transformada
    plt.show()

main()