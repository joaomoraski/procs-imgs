# Como rodar o código em python

É necessário possuir as bibliotecas cv2 e numpy, para obter elas você precisa digitar o comando: 
```
pip install opencv-python
pip install numpy
pip install matplotlib
```
Após isso é só executar o código e responder a pergunta que o programa faz ao ser iniciado.
```
python3 atividade07.py
```
Para fechar o código é so dar um Alt + F4 na tela quando aparecer as imagens

# Respostas Teóricas

### Questão 4
Como o filtro de média é um filtro de suavização, ele tende a atenuar variações abruptas na imagem, como bordas e transições bruscas de cores. Isso significa que as bordas da imagem ficaram menos nítidas ou até mesmo borradas após a aplicação do filtro, que pode depender da intensidade das bordas e do tamanho do filtro utilizado. Esse efeito é comum a todos os filtros de suavização e deve ser considerado ao escolher o filtro mais adequado para cada aplicação.<br>

### Questão 8
O filtro gaussiano 9x9, faz uma suavização melhor que o do filtro de média, isso ocorre porque o filtro gaussiano utiliza uma distribuição para determinar os pesos e leva em consideração a proximidade dos pixels na imagem, então ele possui uma suavização melhor que a do filtro de média.