% G = rand(100,100);
% imshow(G);

G = rand(100,100,3);
% disp(G);
G(19,:,:) = 0;
G(:,40,:) = 1;

% G(:,40,1) = 1;
% G(:,40,2) = 0;
% G(:,40,3) = 0;

RA_sum = 1+9+0+4+0+0+0;

G(19,1:14,1) = 1;
G(19,1:14,2) = 0;
G(19,1:14,3) = 0;


% G(1:14,40,1) = 1;
% G(1:14,40,2) = 0;
% G(1:14,40,3) = 0;
imshow(G);
