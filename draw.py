import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

#img = cv.imread('Photos/cat.jpg')
#cv.imshow('Cat',img)

#blank[200:300, 300:400] = 255,255,0
#cv.imshow('Green',blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2),(255,255,0),thickness=-1)
#cv.imshow('Rectangle',blank)

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
#cv.imshow('Circle',blank)

cv.line(blank,(blank.shape[1]//2,blank.shape[0]//2),(blank.shape[1],blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('Line',blank)

cv.waitKey(0)