######################## P&P Coding Laboratory ##################################
import cv2
import numpy as np
from matplotlib import pyplot as plt

flower = cv2.imread("Images/Flower.jpg")
#flower = cv2.resize(flower, (800,600))
cv2.imshow('original',flower)
cv2.waitKey(0)

#print(s)

flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Binary',flowerGray)
flowerGray = cv2.convertScaleAbs(flowerGray, alpha=1.10 , beta=-20)
#cv2.imshow('Enhance',flowerGray)
#cv2.waitKey(0)

def Hist(image):
    s = image.shape
    H=np.zeros(shape=(256,1))
    for i in range(s[0]):
        for j in range(s[1]):
            k=image[i,j]
            H[k,0]=H[k,0]+1
    return H

H = Hist(flowerGray)
plt.plot(H)
plt.show()

######################## P&P Coding Laboratory ##################################

