imagem = imread("pratica3_reg.gif");
[rotulos, num_rotulos] = rotulacao4con(imagem); % aplica a rotulação de componentes 4-conectadas

disp(num_rotulos);

[~, num_rotulos2] = rotulacao8con(imagem); % aplica a rotulação de componentes 4-conectadas

disp(num_rotulos2);

cores = rand(num_rotulos, 3); % gera uma matriz de cores aleatórias para cada rótulo

imagem_colorida = zeros(size(rotulos, 1), size(rotulos, 2), 3); % cria uma imagem colorida vazia

for i = 1:num_rotulos
    mascara_rotulo = rotulos == i; % cria uma máscara para o rótulo atual
    imagem_colorida(:, :, 1) = imagem_colorida(:, :, 1) + mascara_rotulo .* cores(i, 1); % atribui a cor vermelha
    imagem_colorida(:, :, 2) = imagem_colorida(:, :, 2) + mascara_rotulo .* cores(i, 2); % atribui a cor verde
    imagem_colorida(:, :, 3) = imagem_colorida(:, :, 3) + mascara_rotulo .* cores(i, 3); % atribui a cor azul
end

imshow(imagem_colorida); % exibe a imagem colorida na tela
imwrite(imagem_colorida, "resultadoColorido.png");

%Perus
disp("Perus");

imagem = imread("pratica3_tur.gif");
[rotulos, num_rotulos] = rotulacao4con(imagem); % aplica a rotulação de componentes 4-conectadas

disp(num_rotulos);

[rotulos2, num_rotulos2] = rotulacao8con(imagem); % aplica a rotulação de componentes 4-conectadas

disp(num_rotulos2);

% Como podemos ver o numero resultante da execucao dos mesmos algoritmos
% foi de 0 e 1 para os perus, ou seja, o metodo de rotulacao por 4 ou 8
% conectadas nao foi capaz de reconhecer os 4 perus na imagem

% Definicao das funcoes
function [L, num_labels] = rotulacao4con(A)
    % A função recebe uma imagem binária A e retorna uma imagem rotulada L e o número de rótulos num_labels
    % A imagem rotulada L tem o mesmo tamanho de A e cada pixel é rotulado com um número inteiro indicando sua componente conexa
    % A rotulação segue o critério de similaridade Cs=1 e a conectividade 4

    [nlin, ncol] = size(A);
    L = zeros(nlin, ncol); % inicializa a imagem rotulada com zeros
    next_label = 1; % inicializa o próximo rótulo disponível

    % Varredura da imagem
    for i = 1:nlin

        for j = 1:ncol

            if A(i, j) == 0 % se o pixel é background, passa para o próximo
                continue
            end

            r = 0; t = 0;

            if i > 1
                r = A(i - 1, j); % pixel acima
            end

            if j > 1
                t = A(i, j - 1); % pixel à esquerda
            end

            if r == 0 && t == 0 % nenhum vizinho está rotulado
                L(i, j) = next_label; % rotula com o próximo rótulo disponível
                next_label = next_label + 1;
            elseif r == 1 && t == 0 % vizinho acima está rotulado
                L(i, j) = L(i - 1, j); % rotula com o mesmo rótulo do vizinho acima
            elseif r == 0 && t == 1 % vizinho à esquerda está rotulado
                L(i, j) = L(i, j - 1); % rotula com o mesmo rótulo do vizinho à esquerda
            elseif r == 1 && t == 1 % ambos vizinhos estão rotulados

                if L(i - 1, j) == L(i, j - 1) % vizinhos têm o mesmo rótulo
                    L(i, j) = L(i - 1, j); % rotula com o mesmo rótulo dos vizinhos
                else % vizinhos têm rótulos diferentes
                    L(i, j) = L(i - 1, j); % rotula com o rótulo do vizinho acima
                    L(L == L(i, j - 1)) = L(i - 1, j); % atualiza todos os pixels com o rótulo do vizinho à esquerda
                end

            end

        end

    end

    % Remapeia os rótulos para que sejam números inteiros sequenciais
    labels = unique(L);
    num_labels = numel(labels) - 1; % subtrai 1 porque o label 0 não conta

    for i = 1:num_labels
        L(L == labels(i + 1)) = i; % remapeia para os números inteiros sequenciais
    end

end

function [L, num_labels] = rotulacao8con(imagem)
    % Algoritmo de Rotulação 8-conectada
    % Entrada:
    %   imagem: imagem binária em tons de cinza ou preto e branco
    % Saída:
    %   L: imagem rotulada
    %   num_labels: número de componentes conexos encontrados

    % Obtem as dimensões da imagem
    [linhas, colunas] = size(imagem);

    % Inicializa a matriz de rótulos com zeros
    L = zeros(linhas, colunas);

    % Inicializa o rótulo
    rotulo = 1;

    % Percorre a imagem pixel a pixel
    for i = 1:linhas

        for j = 1:colunas
            % Se o pixel for branco (valor 1)
            if imagem(i, j) == 1
                % Obtem o valor dos pixels vizinhos
                if i == 1
                    r = 0;
                else
                    r = L(i - 1, j);
                end

                if j == 1
                    t = 0;
                else
                    t = L(i, j - 1);
                end

                if i == 1 || j == 1
                    rt = 0;
                else
                    rt = L(i - 1, j - 1);
                end

                if i == 1 || j == colunas
                    lt = 0;
                else
                    lt = L(i - 1, j + 1);
                end

                % Verifica os valores dos pixels vizinhos
                if r == 0 && t == 0 && rt == 0 && lt == 0
                    % Todos os pixels vizinhos são 0
                    % Rotula o pixel com um novo rótulo
                    L(i, j) = rotulo;
                    rotulo = rotulo + 1;
                else
                    % Obtem a lista de rótulos dos pixels vizinhos não nulos
                    rotulos = [r t rt lt];
                    rotulos(rotulos == 0) = [];

                    % Se a lista de rótulos não estiver vazia
                    if ~isempty(rotulos)
                        % Seleciona o menor rótulo
                        menor_rotulo = min(rotulos);
                        % Rotula o pixel com o menor rótulo
                        L(i, j) = menor_rotulo;
                        % Atualiza os rótulos equivalentes
                        rotulos(rotulos == menor_rotulo) = [];

                        for k = 1:length(rotulos)
                            L(L == rotulos(k)) = menor_rotulo;
                        end

                    else
                        % Todos os pixels vizinhos são 0
                        % Rotula o pixel com um novo rótulo
                        L(i, j) = rotulo;
                        rotulo = rotulo + 1;
                    end

                end

            end

        end

    end

    % Obtem o número de componentes conexos encontrados
    num_labels = max(L(:));
end
