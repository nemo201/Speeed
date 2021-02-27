import cv2
import numpy as np

frameWidth = 640    #Frame Width
franeHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500

#img = cv2.imread("car4.jpg", cv2.IMREAD_COLOR) this is not working!!
img = cv2.imread("car3.jpg", cv2.IMREAD_COLOR) #this is working!, area diffrence best guess.
count = 0
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
while 1:
    cv2.imshow("Gray",imgGray)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in numberPlates:
    area = w*h
    if area > minArea:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        imgRoi = img[y:y+h,x:x+w]
        while 1:
            cv2.imshow("ROI",imgRoi)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cv2.imwrite("frame3.jpg",imgRoi)

