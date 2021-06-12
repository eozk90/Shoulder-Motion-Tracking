import cv2
import numpy as np
import time
import PoseModule as pm

#cap = cv2.VideoCapture("Video1.mp4")
cap = cv2.VideoCapture(0)
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280,720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        #Right Arm
        angleRA = detector.findAngle(img,14,12,24)
        #Left Arm
        angleLA = detector.findAngle(img,13,11,23)

        #per = np.interp(angle, (0,90),(0,100))
        #print(angle,per)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
