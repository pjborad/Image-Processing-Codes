######################## Priteh Borad ##################################
import cv2
import numpy as np
shapes = cv2.imread("Images/centroid.jpg")
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
(thresh, shapesBin) = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY)
S = shapes.shape
shapesBin = shapesBin/255
x=0
y=0
n=0
print(shapesBin)
for i in range(S[0]):
    for j in range(S[1]):
        if shapesBin[i,j]==1.0:
            x = x+i
            y = y+j
            n=n+1
x1 = round(x/n)
y1 = round(y/n)
color = (0,0,0)
cv2.circle(shapesBin,(y1,x1),1,color,5)   
cv2.imshow('centroid',shapesBin*255)       
cv2.waitKey(0)  
######################## Priteh Borad ##################################