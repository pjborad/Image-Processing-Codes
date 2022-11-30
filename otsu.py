import numpy as np
import cv2

image = cv2.imread("Images/Flower.jpg")
image = cv2.resize(image,(800,600))
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('binary',image_gray)
#cv2.waitKey(0)

histg = cv2.calcHist([image_gray],[0],None,[255],[0,255])
#histg = np.array([8,7,2,6,9,4])
#histg = np.reshape(histg,(6,1))
within = []
between = []
d=0
for i in range(len(histg)):
    x,y = np.split(histg,[i])
    x1 = np.sum(x)/(image.shape[0]*image.shape[1]) #weight of class 1
    y1 = np.sum(y)/(image.shape[0]*image.shape[1])
    x2 = np.sum([ j*t for j,t in enumerate(x)])/np.sum(x)
    x2 = np.nan_to_num(x2)
    y2 = np.sum([(j+d)*(t) for j,t in enumerate(y)])/np.sum(y)
    x3 = np.sum([(j-x2)**2*t for j,t in enumerate(x)])/np.sum(x)
    x3 = np.nan_to_num(x3)
    y3 = np.sum([(j+d-y2)**2*t for j,t in enumerate(y)])/np.sum(y)
    d=d+1
    within.append(x1*x3 + y1*y3)
    between.append(x1*y1*(x2-y2)*(x2-y2))
m = np.argmin(within)
n = np.argmax(between)
print(m)
print(n)

(thresh, Bin) = cv2.threshold(image_gray,m,255,cv2.THRESH_BINARY)
cv2.imshow("Binary",Bin)
cv2.waitKey(0)