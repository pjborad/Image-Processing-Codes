import numpy as np
import cv2

original = cv2.imread('Images/erosion.jpg')
cv2.imshow('ori',original)
#cv2.waitKey(0)
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
(thresh,bina) = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow('binary',bina)
#cv2.waitKey(0)

filt = np.array([(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1)])
S = bina.shape
F = filt.shape
bina = bina/255
R = S[0]+F[0]-1
C = S[1]+F[1]-1
N = np.zeros((R,C))

for i in range(S[0]):
    for j in range(S[1]):
        N[i+1,j+1]=bina[i,j]

for i in range(S[0]):
    for j in range(S[1]):
        k = N[i:i+F[0],j:j+F[1]]
        result = (k==filt)
        final = np.all(result==True)
        if final:
            bina[i,j]=1
        else:
            bina[i,j]=0
cv2.imshow('final',bina)
cv2.waitKey(0)