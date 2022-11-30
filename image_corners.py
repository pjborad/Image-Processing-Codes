######################## Priteh Borad ##################################
import cv2
import numpy as np

shapes = cv2.imread("Images/corners.jpg")
#shapes = cv2.resize(shapes, (400,400))

filt1 = np.array([(25,1,25),(0,1,1),(0,0,25)])
filt2 = np.array([(25,1,25),(1,1,0),(25,0,0)])
filt3 = np.array([(25,0,0),(1,1,0),(25,1,25)])
filt4 = np.array([(0,0,25),(0,1,1),(25,1,25)])
S = shapes.shape
F = filt1.shape
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
(thresh, shapesBin) = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY)
shapesBin = shapesBin/255
cv2.imshow('original',shapesBin)
R = S[0]+F[0]-1
C = S[1]+F[1]-1
N = np.zeros((R,C))  
def Nanfillcompare(y,filt):
 z = np.array([0,0,0,0,0,0,0,0,0])
 for i in range(9):
    y=y.flatten()
    filt=filt.flatten()
    if filt[i] == 25:
        z[i]=1
    elif y[i]==filt[i]:
        z[i]=1    
 if np.all(z == 1):
     return True
 else:
     return False 
for i in range(S[0]):
    for j in range(S[1]):
        N[i+1,j+1]=shapesBin[i,j]     

for i in range(S[0]):
    for j in range(S[1]):     
        k = N[i:i+F[0],j:j+F[0]]
        t=np.array([Nanfillcompare(k,filt1),Nanfillcompare(k,filt2),Nanfillcompare(k,filt3),Nanfillcompare(k,filt4)])
        #print(t)
        result = np.any(t == True)
#        print(result)
        color=(1,1,1)
        if result: 
            cv2.circle(shapesBin,(j,i),5,color)
#        else:
#            shapesBin[i,j]=0
cv2.imshow('mycorners',shapesBin*255)
#cv2.imshow('dilatoion',img_dilation)
cv2.waitKey(0)   
######################## Priteh Borad ##################################
    
