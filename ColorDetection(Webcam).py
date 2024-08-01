import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(1)  # Change to 0 to use the default camera
cap.set(2, frameWidth)
cap.set(2, frameHeight)


def empty(a):
    pass

#Creates Trackbar
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640,280)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)


while True:
    sucess,img = cap.read() 
    
    
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    
    # Apply morphological operations to clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)
    mask = cv2.dilate(mask, kernel)
    
    result = cv2.bitwise_and(img, img, mask = mask)
    
    
    


    cv2.imshow("Original Video", img)
    cv2.imshow('HSV Image', imgHsv)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result Image', result)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):      #Press 'q' to stop the code
        break


cap.release()
cv2.destroyAllWindows() 