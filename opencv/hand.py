import cv2 
import numpy as np

img = cv2.imread('img.png', 0)

ret, trace = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#_,contours,_ = cv2.findContours(trace,  cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
major = cv2.__version__.split('.')[0]
if major == '0':
    ret, contours, hierarchy = cv2.findContours(trace.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
else:
    contours, hierarchy = cv2.findContours(trace.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


hull = [cv2.convexHull(c) for c in contours]

final = cv2.drawContours(img, hull, -1, (0,0,255),3)

cv2.imshow("orginal image", img)
cv2.imshow("thresh", trace)
cv2.imshow("convex Hull", final)

cv2.waitKey(0)
cv2.destroyAllWindows()