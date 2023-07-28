img = imread('pratica6.png');
ruido = normrnd(0, 64/256, size(img));
img_ruidosa = im2double(img) + ruido;
figure;
subplot(2,1,1); imhist(img); title('Histograma da imagem original');
subplot(2,1,2); histogram(img_ruidosa(:)); title('Histograma da imagem com ruído');

diferenca = calc_diferenca(img, img_ruidosa);


function diferenca = calc_diferenca(img1, img2)
    hist1 = imhist(img1);
    hist2 = imhist(img2);
    diferenca = norm(hist1 - hist2);
end
