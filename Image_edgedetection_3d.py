import cv2
import numpy as np

def Mean(image,kernal):
    S = image.shape
    F = kernal.shape
    R = S[0]+F[0]-1
    C = S[1]+F[1]-1
    N = np.zeros((R,C)) 
    for i in range(S[0]):
        for j in range(S[1]):
            N[i+1,j+1]=image[i,j]   
    for i in range(S[0]):
        for j in range(S[1]):
            k = N[i:i+F[0],j:j+F[0]]
            k = np.sum(k*kernal)
            image[i,j]=np.abs(k) 
    return image 

def edge_detection(image):
    filt = np.array([(0,0,-1,0,0),(0,-1,-2,-1,0),(-1,-2,16,-2,-1),(0,-1,-2,-1,0),(0,0,-1,0,0)])/25
    filt = np.array([(-1,-1,-1),(-1,8,-1),(-1,-1,-1)])
    image = Mean(image,filt)
    return image  

image = cv2.imread('noise1.jpg')
#image = cv2.resize(image,(400,300))
cv2.imshow('initial',image)
b,g,r = cv2.split(image)

b1 = edge_detection(b)
g1 = edge_detection(g)
r1 = edge_detection(r)

final = cv2.merge((b1,g1,r1))
cv2.imshow('Fianl',final)
cv2.waitKey(0)