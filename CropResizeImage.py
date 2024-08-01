import cv2

img = cv2.imread("Resources/road.jpg")
print(img.shape)                                    #Prints image dimension(pixels)

width, height = 400, 400                            #declaring image new pixels
imgResize = cv2.resize(img,(width,height))          #Resizes the image
print(imgResize)


imgCropped = img[200:400, 0:714]                    #Crops the image

cv2.imshow("Road", img)
cv2.imshow("Road Resized", imgResize)
cv2.imshow("Road Cropped", imgCropped)
cv2.waitKey(0)