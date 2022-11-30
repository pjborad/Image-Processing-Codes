import cv2
import numpy as np

original = cv2.imread('Images/princeton_small.jpg')
cv2.imshow('original',original)
s = original.shape
#print(original[1:2,:,:])
scale = -0.5
black = np.zeros((s[0],s[1],s[2]))
black[black==0]=127
x = np.zeros((s[0],s[1],s[2]))
for i in range(s[0]):
    for j in range(s[1]):
        for k in range(s[2]):
            x[i,j,k] = np.clip((1-scale)*black[i,j,k] + scale*original[i,j,k], 0, 255) 
x = x.astype(np.uint8)
#print(x[1:2,:,:])

cv2.imshow('final',x)
cv2.waitKey(0)

