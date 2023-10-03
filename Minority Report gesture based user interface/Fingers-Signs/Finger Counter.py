import cv2
import time
import os

width,height = 1080,720

vidCapture = cv2.VideoCapture(0)
vidCapture.set(3,width)
vidCapture.set(4,height)

folderPath = "FingerSigns"
mySigns = os.listdir(folderPath)
print(mySigns)



while True:

    success,img =vidCapture.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)