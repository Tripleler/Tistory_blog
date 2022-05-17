import sys
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

symmetric = False
auto = True
delay = 3
i = 0

while True:
    i += 1
    if i > 10000:
        i = 1

    ret, frame = cap.read()

    if not ret:
        break

    if auto:
        cv2.imshow('frame', frame) if symmetric else cv2.imshow('frame', frame[:, ::-1])
        if i % delay == 0:
            symmetric = False if symmetric else True
    else:
        cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == ord('a'):
        auto = False if auto else True
    if key == ord('i'):
        delay = 10
    if key == ord('o'):
        delay = 3
    if key == ord('p'):
        delay = 1

cap.release()
cv2.destroyAllWindows()
