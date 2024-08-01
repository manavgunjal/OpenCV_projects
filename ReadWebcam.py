import cv2

frameWidth = 360
frameHeight = 360

cap = cv2.VideoCapture(1)    #0 for inbuilt camera, 1 for external camera
cap.set(3,frameWidth)
cap.set(4,frameHeight)

while True:
    sucess, img = cap.read()     
    cv2.imshow("Video", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  #press 'q' to exit the webcam
        break