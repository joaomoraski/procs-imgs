# Como rodar o código em python

É necessário possuir as bibliotecas cv2 e numpy, para obter elas você precisa digitar o comando: 
```
pip install opencv-python
pip install numpy
pip install matplotlib
```
Após isso é só executar o código e responder a pergunta que o programa faz ao ser iniciado.
```
python3 pratica4.py
```

# Respostas Teóricas.

Todos as imagens e casos de testes estão no código, porém caso queira abrir as imagens e visualizá-las são as que estão no arquivo zip<br>
Casos de teste:<br>
    entradasR = [[0, 69, 185 , 255], [69, 69, 200, 255], [25, 125,200,140], [198,248,95,195]]<br>
    entradasS = [[0, 124, 161, 255], [0,161,124,255], [20,15,88,99], [220,188,177,222]]<br>

### Questão 4
Para um caso da imagem ser mais clara, você precisaria colocar valores de saída maiores do que os de entrada, um exemplo seria: r = [0, 50, 150, 255] e s = [0, 100, 200, 255]. Isso ocorre porque o pixel vai ser mapeado em um valor mais alto no intervalo de [0, 255].
___
Em casos de imagens mais escuras, pode-se diminuir os valores de saída, em relação aos valores de entrada, um exemplo seria r = [0, 50, 150, 255] e s = [0, 50, 100, 255]. Isso ocorre porque o pixel vai ser mapeado em um valor mais baixo no intervalo de [0, 255].
___
Para reduzir o contraste da imagem, pode-se diminuir a diferença entre os valores dos pontos de saída adjacentes, um exemplo seria: r = [0, 50, 150, 255] e s = [0, 150, 150, 255]. Isso ocorre porque a imagem resultante terá menos contraste do que a imagem original, pois a diferença entre os valores de saída adjacentes é menor.
___
Para aumentar o contraste da imagem, pode-se aumentar a diferença entre os valores dos pontos de saída adjacentes, um exemplo seria: r = [0, 50, 150, 255] e s = [0, 25, 225, 255], Isso ocorre porque a imagem resultante terá mais contraste do que a imagem original, pois a diferença entre os valores de saída adjacentes é maior.
___
O algoritmo Piecewise Linearization é reversível, porém só quando se conhece os pontos de entrada e saída originais. Caso não seja conhecido, a imagem resultante não pode ser revertida para a imagem original. Em alguns casos podem ocorrer a perda de alguns pixels, então caso tenha alguns detalhes sutis e importantes eles podem acabar se perdendo e impedindo a reversão.
___