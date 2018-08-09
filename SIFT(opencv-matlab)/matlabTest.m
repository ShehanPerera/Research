%Convert images in to gray scale 
img1= imread('1.jpg');
img1= rgb2gray(img1);
imwrite(img1,'img1.pgm');

img2= imread('2.jpg');
img2= rgb2gray(img2);
imwrite(img2,'img2.pgm');
% To get descriptors
[image1, descrips1, locs1] = sift('img1.pgm');
[image2, descrips2, locs2] = sift('img2.pgm');
% To match images
num = match('img1.pgm','img2.pgm');