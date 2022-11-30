######################## Priteh Borad ##################################
import cv2
import numpy as np
corela = cv2.imread("Images/corelation.jpeg")
corela = cv2.resize(corela, (900,700))

filt = cv2.imread("Images/core_kernal.jpg")
filt = cv2.resize(filt, (141,141))
S = corela.shape
F = filt.shape
#print(F)
shapeGray = cv2.cvtColor(corela, cv2.COLOR_BGR2GRAY)
#shapeGray = cv2.convertScaleAbs(shapeGray, alpha=1.1 , beta=-20)/255
#shapeGray = cv2.threshold(shapeGray, 127, 255, cv2.THRESH_BINARY)
filt = cv2.cvtColor(filt, cv2.COLOR_BGR2GRAY)
#filt = cv2.threshold(filt, 127, 255, cv2.THRESH_BINARY)
#filt = cv2.convertScaleAbs(filt, alpha=1.1 , beta=-20)
cv2.imshow('original',shapeGray)
#cv2.imshow('shape',filt)
#cv2.waitKey(0)   
R = S[0]+F[0]-1
C = S[1]+F[1]-1
N = np.zeros((R,C)) 
      
for i in range(S[0]):
    for j in range(S[1]):
        N[i+1,j+1]=shapeGray[i,j]        

for i in range(S[0]):
    for j in range(S[1]):
        k = N[i:i+F[0],j:j+F[0]]
        k = np.sum(k*filt)/(151*151*255)
        shapeGray[i,j]=k

cv2.imshow('corelation',shapeGray)
#cv2.imwrite('Flowergaussian.jpg',shapeGray)
cv2.waitKey(0) 
######################## Priteh Borad ##################################    


