######################## Priteh Borad ##################################
import cv2
import numpy as np

original = cv2.imread('Images/flower.jpg')
original = cv2.resize(original, (900,700))
compres = cv2.imread('Images/flower.jpg')
compres = cv2.resize(compres, (800,600))

cv2.imshow('original',original)
cv2.imshow('compressed',compres)
shape1 = original.shape
shape2 = compres.shape
size1 = shape1[0]*shape1[1]*shape1[2]/(1024*1024)
print("size of original image is" , size1,"MB" )
size2 = shape2[0]*shape2[1]*shape2[2]/(1024*1024)
print("size of compressed image is", size2,"MB")
compression_ration = size1/size2
print("Compression ration is", compression_ration)
cv2.waitKey(0)
######################## Priteh Borad ##################################