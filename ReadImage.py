import cv2

img = cv2.imread("Resources/Lena.png")

cv2.imshow("Lena", img)

cv2.waitKey(0)