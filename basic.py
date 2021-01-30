import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cany = cv.Canny(img, 150,150)
cv.imshow('Cany', cany)

dilated = cv.dilate(cany, (7,7), iterations=1)
cv.imshow('Dilated',dilated)

cropped = img[100:300, 100:300]
cv.imshow('Cropped',cropped)

cv.waitKey(0)