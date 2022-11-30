######################## Priteh Borad ##################################
import cv2
import numpy as np
flower = cv2.imread("Images/FlowerPepper.jpg")
flower = cv2.resize(flower, (800,600))
flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)
flowerGray = cv2.convertScaleAbs(flowerGray, alpha=1.1 , beta=-20)
cv2.imshow('original',flowerGray)
S = flower.shape
N = np.zeros((602,802)) 

for i in range(S[0]):
    for j in range(S[1]):
        N[i+1,j+1]=flowerGray[i,j]

for i in range(S[0]):
    for j in range(S[1]):
        k = N[i:i+3,j:j+3]
        k = np.median(k)
        flowerGray[i,j]=k
print(flowerGray)
cv2.imshow('median',flowerGray)
cv2.waitKey(0)
######################## Priteh Borad ##################################