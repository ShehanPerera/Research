import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read image 
img1 = cv2.imread('basmati.pgm')
img2 = cv2.imread('basmati2.pgm') 

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# Convering to Gray
img1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# no.of keypoints 
print(len(des1))
print(len(des2))

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Create images with keypoints
img1=cv2.drawKeypoints(img1,kp1,img1)
cv2.imwrite('2sift_keypoints.jpg',img1)

img2=cv2.drawKeypoints(img2,kp2,img2)
cv2.imwrite('3sift_keypoints.jpg',img2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

print("matches ")
print(len(good))

