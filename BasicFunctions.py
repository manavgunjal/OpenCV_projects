import cv2

img = cv2.imread("Resources/Lena.png")    
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #Png image is converted in grayscale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)      #Grayscale image is converted into blur (7,7) is the blur intensity which is always in even number
imgCanny = cv2.Canny(imgGray, 100, 100)          #Canny is kind of filter/effect for the image. (100,100) is the threshold which can be adjustable


cv2.imshow("Lena", img)                #Open's a normal png image
cv2.imshow("GrayScale", imgGray)       #Open's grayscale image
cv2.imshow("Blur Image", imgBlur)      #Open's blurred grayscale image
cv2.imshow("Canny Image", imgCanny)    #Open's canny image


cv2.waitKey(0)  #