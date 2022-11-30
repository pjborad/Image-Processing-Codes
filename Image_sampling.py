import cv2
import numpy as np
import inspect
#cv2.namedWindow("original",cv2.WINDOW_NORMAL)
image = cv2.imread('Images/noise1.jpg')
b,g,r = cv2.split(image)
cv2.imshow('original',image)
print(image.shape)
def point(image, h_scale, w_scale):
    s = image.shape
    h= np.round(s[0]*h_scale)
    h = h.astype(int)
    w = np.round(s[1]*w_scale)
    w = w.astype(int)
    final = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            final[i,j] = image[np.int(np.round(i/h_scale))-1,np.int(np.round(j/w_scale))-1]
    final = final.astype(np.uint8)   
    return final
#final = point(image,0.3,0.3)


def bilinear(image, h_scale, w_scale):
    s = image.shape
    h= np.round(s[0]*h_scale)
    h = h.astype(int)
    w = np.round(s[1]*w_scale)
    w = w.astype(int)
    final = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            W = -((i/h_scale)-np.floor(i/h_scale)-1)
            H = -((j/w_scale)-np.floor(j/w_scale)-1)
            I11 = image[np.int(np.floor(i/h_scale))-1,np.int(np.floor(j/w_scale))-1]
            I12 = image[np.int(np.ceil(i/h_scale))-1,np.int(np.floor(j/w_scale))-1]
            I21 = image[np.int(np.floor(i/h_scale))-1,np.int(np.ceil(j/w_scale))-1]
            I22 = image[np.int(np.ceil(i/h_scale))-1,np.int(np.ceil(j/w_scale))-1]
            final[i,j] = (1-W)*(1-H)*I22 + (W)*(1-H)*I21 + (1-W)*(H)*I12 + (W)*(H)*I11
    final = final.astype(np.uint8)
    return final


b = bilinear(b,3,3)
g = bilinear(g,3,3)
r = bilinear(r,3,3)
final = cv2.merge((b,g,r))
cv2.imshow('final',final)
cv2.waitKey(0)