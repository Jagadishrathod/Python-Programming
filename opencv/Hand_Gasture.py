import cv2
import numpy as np 
import math

capture = cv2.VideoCapture(0)

while capture.isOpened():

    # Capture frames from the camera
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    # Get hand data from the rectangle sub window
    cv2.rectangle(frame, (10, 10), (300, 300), (0,255, 0), 0) # start_end, end_point, color = (255, 0, 0), thickness = 0
    crop_image = frame[10:300, 10:300]

    # Apply Gaussian blur
    # blur = cv2.GaussianBlur(crop_image, (3,3), 0)  

    # Change color-space from BGR -> HSV
    hsv = cv2.cvtColor(crop_image, cv2.COLOR_BGR2HSV)

    # Create a binary image with where White will be skin colors and rest is black
    mask2 = cv2.inRange(hsv, np.array([0, 48, 80]), np.array([20, 255, 255]))

    # Kernel for morphological transformation
    kernel = np.ones((5,5), np.uint8)

    # Apply morphologial transformations to filter out the background noise
    dilation = cv2.dilate(mask2, kernel, iterations = 1)
    erosion = cv2.erode(dilation, kernel, iterations = 1)

    # Apply Gaussian Blur and Threshold
    filtered = cv2.GaussianBlur(erosion, (3, 3), 0)
    ret, thresh = cv2.threshold(filtered, 200, 25, cv2.THRESH_BINARY)
    # ret, thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    
    drawing = np.zeros(crop_image.shape, np.uint8)

    # Show threshold image
    cv2.imshow("Thresholded", thresh)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find contour with maximum area
    contour = max(contours, key = lambda x: cv2.contourArea(x))

    # Create bounding rectangle around the contour
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)

    # Find convex hull
    hull = cv2.convexHull(contour)

    # Draw contour
    drawing = np.zeros(crop_image.shape, np.uint8)
    cv2.drawContours(drawing, [contour], 0, (0, 255, 0), 2)
    cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3) 

    # Find convexity defects
    hull = cv2.convexHull(contour, returnPoints = False)
    defects = cv2.convexityDefects(contour, hull)

    count_defects = 0

    for i in range(defects.shape[0]):

        s,e,f,d = defects[i, 0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])

        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
        angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2* b * c)) * 180) / 3.14

            # if angle > 90 draw a circle at the far point 
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_image, far, 1, [0, 0, 255], -1)

        cv2.line(crop_image, start, end, [0, 255, 0], 2)

            # Print number of fingers
        if count_defects == 1:
            cv2.putText(frame, "[1]", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 2:
            cv2.putText(frame, "[2]", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 3:
            cv2.putText(frame,"[3]", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 4:
            cv2.putText(frame,"[4]", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        else:
            cv2.putText(frame,"[5]", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

    # Show required images
    cv2.imshow("Gesture", frame)
    all_image = np.hstack((drawing, crop_image))
    cv2.imshow('contours', all_image)

        # Close the camera if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()