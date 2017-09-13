#!/usr/bin/python
# replay captured images like a video
# JMS 2017
#

import cv2
import time

print("Press 'q' to stop.")

i=0
cap = cv2.VideoCapture("snapshot-%08d.jpg")
while True:
    ret, image = cap.read()
    if not ret: break

    cv2.imshow(" ", image)
    i += 1
    k=cv2.waitKey(100)
    if k & 0xFF == ord('q'):
        print("stop")
        break

cap.release()           # clear buffer
print("finished. processed {} images.".format(i))
