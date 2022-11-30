import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
flower = cv2.imread("Images/Flower.jpg")
flower = cv2.resize(flower, (800,600))
s = flower.shape
flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)
flowerGray = cv2.convertScaleAbs(flowerGray, alpha=1.10, beta=40)
#print(flowerGray)
#print(flowerGray[0,1])
#cv2.imshow('flower',flower)
#cv2.imshow('flowerGray',flowerGray)
#cv2.waitKey(0)
histg = cv2.calcHist([flowerGray],[0],None,[256],[0,256]) #None for full  image #0 for gray scale#
#print(histg)
x = histg.reshape(1,256)
y=np.zeros(shape=(1,256))
for i in range(256): 
    if x[0,i]==0:
        y[0,i]=0
    else:
        y[0,i]=i   

for i in range(256):  # finding Min and Max
    if y[0,i]==0:
        continue
    elif y[0,i]!=0:
        min = y[0,i]
        break
max = y.max(1)

strech = np.round((255/(max-min))*(y-min))

for i in range(256):
    if strech[0,i]<0:
        strech[0,i]=0
    elif strech[0,i]>255:
        strech[0,i]=255
for i in range(s[0]-1):
    for j in range(s[1]-1):
        k = flowerGray[i,j]
        flowerGray[i,j] = strech[0,k]
histg2 = cv2.calcHist([flowerGray],[0],None,[256],[0,256])      
#cv2.imshow('mysteching',flowerGray)
#cv2.waitKey(0)
plt.plot(histg)
plt.plot(histg2)
plt.show()

     
