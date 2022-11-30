######################## Priteh Borad ##################################
import numpy as np
import cv2

array1 = np.array([8, 4, 9,1,21,19,14,34,28, 11, 17, 15,8,31,14,7])
#array1 = cv2.imread('Morph1.jpg')
#array1 = cv2.resize(array1, (700,700))
#array1 = cv2.cvtColor(array1, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',array1)
#array1 = array1.flatten()
#(thresh, flowerBin) = cv2.threshold(flowerGray, 127, 255, cv2.THRESH_BINARY)
centroid = np.array([1 ,11 ,18])
#x = np.array([]) 
z = np.zeros((len(centroid),len(array1)))
for i in range(10):
    for i in range(len(centroid)):
        z[i,0:len(array1)]=np.absolute(array1 - centroid[i])

    x = np.argmin(z,axis=0)
    #print(x)
    for i in range(len(array1)):
        x[i] = centroid[x[i]]    

    for i in range(len(centroid)):
        t = (x==centroid[i])
        d=array1[t]
        e = np.around(np.sum(d)/len(d))
        centroid[i]=e
        print(centroid)      
"""
q=0
for i in range(len(centroid)):
    a = (x==centroid[i])
    array1[a]=0+q
    q=255
x = np.reshape(x,(700,700))
print(x)
#cv2.imshow('segmentation',x)"""
#cv2.waitKey(0)
######################## Priteh Borad ##################################