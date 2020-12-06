import cv2 
import numpy as np 
  

I = rgb2gray(imread("flowers.jpg")); 
subplot(2, 4, 1), 
imshow(I); 
title("Gray Scale Image"); 

 
J = edge(I, 'Sobel'); 
subplot(2, 4, 2), 
imshow(J); 
title("Sobel"); 

K = edge(I, 'Prewitt'); 
subplot(2, 4, 3), 
imshow(K); 
title("Prewitt"); 

 
L = edge(I, 'Roberts'); 
subplot(2, 4, 4), 
imshow(L); 
title("Robert"); 

M = edge(I, 'log'); 
subplot(2, 4, 5), 
imshow(M); 
title("Log"); 

M = edge(I, 'zerocross'); 
subplot(2, 4, 6), 
imshow(M); 
title("Zerocross"); 

N = edge(I, 'Canny'); 
subplot(2, 4, 7), 
imshow(N); 
title("Canny"); 

