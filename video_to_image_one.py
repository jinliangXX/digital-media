import cv2
import numpy

cap = cv2.VideoCapture('img.mp4')

while cv2.waitKey(30) != ord('q'):
    retval, image = cap.read()
    cv2.imshow("video", image)
cap.release()
