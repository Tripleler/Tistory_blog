import sys
import cv2
import random
import numpy as np

# read image
img = cv2.imread('../icon/logo.png')
if img is None:
    print('Image load failed!')
    sys.exit()

# resize
img = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
height, width, _ = img.shape
center = (width / 2, height / 2)
print(img.shape)

while True:
    # flip with cv2 library
    img2 = cv2.flip(img, 0)  # flip-ud
    img3 = cv2.flip(img, 1)  # flip-lr

    # flip with affine matrix
    # T1 = np.eye(3)
    # T1[0, 2], T1[1, 2] = center
    #
    # T2 = np.eye(3)
    # T2[0, 2], T2[1, 2] = -center[0], -center[1]
    #
    # UD = np.eye(3)
    # UD[1, 1] = -1
    # UD = T1 @ UD @ T2
    #
    # LR = np.eye(3)
    # LR[0, 0] = -1
    # LR = T1 @ LR @ T2
    #
    # img2 = cv2.warpAffine(img, UD[:2], dsize=(width, height), borderValue=(114, 114, 114))
    # img3 = cv2.warpAffine(img, LR[:2], dsize=(width, height), borderValue=(114, 114, 114))

    cv2.imshow('Raw', img[:, :, ::-1])
    cv2.imshow('UD-flip', img2[:, :, ::-1])
    cv2.imshow('LR-flip', img3[:, :, ::-1])
    cv2.moveWindow('Raw', 50, 250)
    cv2.moveWindow('UD-flip', 700, 250)
    cv2.moveWindow('LR-flip', 1350, 250)

    key = cv2.waitKey()
    if key == 27:
        break
cv2.destroyAllWindows()
