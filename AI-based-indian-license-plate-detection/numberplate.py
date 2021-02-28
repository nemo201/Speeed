import cv2
import numpy as np

frameWidth = 640    #Frame Width
franeHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier("indian_license_plate.xml")
minArea = 500

img = cv2.imread("images.jpg", cv2.IMREAD_COLOR)
count = 0
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in numberPlates:
    area = w*h
    if area > minArea:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        imgRoi = img[y:y+h,x:x+w]
        cv2.imshow("ROI",imgRoi)
        cv2.imwrite("frame3.jpg",imgRoi)


