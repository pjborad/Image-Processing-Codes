######################## Priteh Borad ##################################
import cv2
import numpy as np
flower = cv2.imread("Images/home.jpeg")
#flower = cv2.resize(flower, (800,600))
filt = np.array([(0,0,-1,0,0),(0,-1,-2,-1,0),(-1,-2,16,-2,-1),(0,-1,-2,-1,0),(0,0,-1,0,0)])/25 #laplacian of guassian
#filt = np.array([(-1,-1,-1),(-1,8,-1),(-1,-1,-1)])/9  #simple edge detection
S = flower.shape
F = filt.shape
flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)
flowerGray = cv2.convertScaleAbs(flowerGray, alpha=1.4 , beta=40)
cv2.imshow('original',flowerGray)
R = S[0]+F[0]-1
C = S[1]+F[1]-1
N = np.zeros((R,C)) 
      
for i in range(S[0]):
    for j in range(S[1]):
        N[i+1,j+1]=flowerGray[i,j]        

for i in range(S[0]):
    for j in range(S[1]):
        k = N[i:i+F[0],j:j+F[0]]
        k = np.sum(k*filt)
        flowerGray[i,j]=k

cv2.imshow('edge',flowerGray)
#cv2.imwrite('Flowergaussian.jpg',flowerGray)
cv2.waitKey(0)     
######################## Priteh Borad ##################################

