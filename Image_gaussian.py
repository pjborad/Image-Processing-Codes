import cv2
import pandas as pd
import numpy as np
import math

image = cv2.imread('Images/noise1.jpg')
#print(image[1,:])
#image = cv2.resize(image,(400,300))
#print(image[1,:])
cv2.imshow('initial',image)
b,g,r = cv2.split(image)

def Mean(image,kernal):
    S = image.shape
    F = kernal.shape
    R = S[0]+F[0]-1
    C = S[1]+F[1]-1
    N = np.zeros((R,C)) 
    for i in range(S[0]):
        for j in range(S[1]):
            N[i+np.int((F[0]-1)/2),j+np.int((F[1]-1)/2)]=image[i,j]   
    for i in range(S[0]):
        for j in range(S[1]):
            k = N[i:i+F[0],j:j+F[0]]
            k = np.sum(k*kernal)
            image[i,j]=k 
    return image  

sigma = 5
x = np.ceil(3*sigma)*2 + 1
x = x.astype(np.uint8)
filter = np.zeros((x,x))
s = filter.shape
t = np.ceil(s[0]/2)
for i in range(x):
    for j in range(x):
        filter[i,j] = math.exp(-((i-t)**2 + (j-t)**2)/(2*(sigma**2)))/(2*math.pi*(sigma**2))
print(filter)
b1 = Mean(b,filter)
g1 = Mean(g,filter)
r1 = Mean(r,filter)

final = cv2.merge((b1,g1,r1))
cv2.imshow('final',final)
cv2.waitKey(0)