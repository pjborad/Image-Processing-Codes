import numpy as np
import cv2

original = cv2.imread('Images/Morph3.jpg')
cv2.imshow('ori',original)
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
(thresh,bina) = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

filt = np.array([(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1)])

def erosion(img,filt):
    S = img.shape
    F = filt.shape
    img = img/255
    R = S[0]+F[0]-1
    C = S[1]+F[1]-1
    N = np.zeros((R,C))

    for i in range(S[0]):
        for j in range(S[1]):
            N[i+1,j+1]=img[i,j]

    for i in range(S[0]):
        for j in range(S[1]):
            k = N[i:i+F[0],j:j+F[1]]
            result = (k==filt)
            final = np.all(result==True)
            if final:
                img[i,j]=1
            else:
                img[i,j]=0
    return img*255

def dilation(img,filt):
    S = img.shape
    F = filt.shape
    img = img/255
    R = S[0]+F[0]-1
    C = S[1]+F[1]-1
    N = np.zeros((R,C))

    for i in range(S[0]):
        for j in range(S[1]):
            N[i+1,j+1]=img[i,j]

    for i in range(S[0]):
        for j in range(S[1]):
            k = N[i:i+F[0],j:j+F[1]]
            result = (k==filt)
            final = np.any(result==True)
            if final:
                img[i,j]=1
            else:
                img[i,j]=0
    return img*255

def closing(img,filt):
    c1 = dilation(bina,filt)
    c2 = erosion(c1,filt)
    return c2

def opening(img,filt):
    o1 = erosion(bina,filt)
    o2 = dilation(o1,filt)
    return o2

final = closing(bina,filt)
cv2.imshow('final',final)
cv2.waitKey(0)