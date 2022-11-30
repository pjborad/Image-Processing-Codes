import cv2
import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

back = cv2.imread('Images/comp_background.jpg')
fore = cv2.imread('Images/comp_foreground.jpg')
mask = cv2.imread('Images/comp_mask.jpg')
#mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
mask = mask/255
#mask = mask.astype(float)/255
#back = back.astype(float)
#fore = fore.astype(float)
#(thresh, mask) = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
#print(mask)
#b_back = back[:,:,0]
#g_back = back[:,:,1]
#r_back = back[:,:,2]

#b_fore = fore[:,:,0]
#g_fore = fore[:,:,1]
#r_fore = fore[:,:,2]

s = back.shape
x = np.zeros((s[0],s[1],s[2]))
for i in range(s[0]):
    for j in range(s[1]):
        for k in range(s[2]):
            x[i,j,k]= np.clip(fore[i,j,k]*mask[i,j,0] + back[i,j,k]*(1-mask[i,j,0]),0,255)

x = x.astype(np.uint8)
cv2.imshow('final',x)
cv2.waitKey(0)
