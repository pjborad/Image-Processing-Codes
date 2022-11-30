######################## P&P Coding Lab ##################################
import cv2
import numpy as np
from scipy import stats

flower = cv2.imread("Images/FlowerSalt.jpg")
flower = cv2.resize(flower, (800,600)) #Resizing the image
#filt = np.array([(1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1)])*(1/25) #filter (5,5)
filt = np.array([(1,1,1),(1,1,1),(1,1,1)])*(1/9) #filter (3,3)
S = flower.shape
F = filt.shape
flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY) #binary conversion
cv2.imshow('original',flowerGray)

R = S[0]+F[0]-1
C = S[1]+F[1]-1
Z = np.zeros((R,C))

for i in range(S[0]):
    for j in range(S[1]):
        Z[i+np.int((F[0]-1)/2),j+np.int((F[1]-1)/2)] = flowerGray[i,j]

print(Z)        

"""
for i in range(S[0]):
    for j in range(S[1]):
        k = Z[i:i+F[0],j:j+F[1]]
        l = stats.mode(k,axis=None)
        flowerGray[i,j]=l[0][0]
cv2.imshow('final',flowerGray)
cv2.waitKey(0)

"""




      



for i in range(S[0]):
    for j in range(S[1]):
        k = Z[i:i+F[0],j:j+F[0]]
        k = np.sum(k*filt)
        flowerGray[i,j]=k

cv2.imshow('lowpass',flowerGray)
#cv2.imwrite('Flowergaussian.jpg',flowerGray)
cv2.waitKey(0)
   
######################## Priteh Borad ##################################

