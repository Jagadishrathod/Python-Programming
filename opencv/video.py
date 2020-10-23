import cv2 

Capture = cv2.VideoCapture(0) 
  
while(True): 
    ret, frame = Capture.read() 

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ret, thresh1 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV) 
    ret, thresh3 = cv2.threshold(img, 80, 255, cv2.THRESH_TRUNC) 
    ret, thresh4 = cv2.threshold(img, 80, 255, cv2.THRESH_TOZERO) 
    ret, thresh5 = cv2.threshold(img, 80, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow('Threshold', thresh1)
    cv2.imshow('Binary Threshold Inverted', thresh2) 
    cv2.imshow('Truncated Threshold', thresh3) 
    cv2.imshow('Set to 0', thresh4) 
    cv2.imshow('Set to 0 Inverted', thresh5) 

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

Capture.release() 
cv2.destroyAllWindows() 