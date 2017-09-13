#!/usr/bin/python
# capture an image every x seconds 
# JMS 2017
#
WAIT=60 # sleep time in seconds

import cv2
import time

print("Press 'q' to stop.")
i=730

while True:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ,1024)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 576)
    ret, image = cap.read()
    print(ret)
    cap.release()           # clear buffer
    if not ret: 
        print("ret nonzero")
        break

    output = "snapshot-{:08}.jpg".format(i) # 8 digits, leading zeros
    cv2.imwrite(output, image)
    i += 1
    
    cv2.imshow(" ", image)
    k=cv2.waitKey(1000*WAIT)
    if k & 0xFF == ord('q'):         # does not work, always -1
        print("stop")
        break

    print(time.strftime("%d %b %Y %H:%M:%S",time.localtime()))
