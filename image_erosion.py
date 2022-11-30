######################## Priteh Borad ##################################
import cv2
import numpy as np
shapes = cv2.imread("Images/erosion.jpg")
filt = np.array([(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1)])
S = shapes.shape
print(S)
F = filt.shape
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
(thresh, shapesBin) = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY)
shapesBin = shapesBin/255
cv2.imshow('original',shapesBin)
R = S[0]+F[0]-1
C = S[1]+F[1]-1
N = np.zeros((R,C))  
for i in range(S[0]):
    for j in range(S[1]):
        N[i+1,j+1]=shapesBin[i,j]        
for i in range(S[0]):
    for j in range(S[1]):
        k = N[i:i+F[0],j:j+F[0]]
        z=(k==filt)
        result = np.all(z == True)
        if result:
            shapesBin[i,j]=1
        else:
            shapesBin[i,j]=0
        
cv2.imshow('myerosion',shapesBin*255)
cv2.waitKey(0)   
######################## Priteh Borad ##################################
