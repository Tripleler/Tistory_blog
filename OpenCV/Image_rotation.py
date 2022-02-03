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
print(img.shape)
degrees = 90

while True:
    a = random.uniform(-degrees, degrees)
    print(f'회전각:{round(a, 2)}도')
    R = cv2.getRotationMatrix2D(angle=a, center=(width / 2, height / 2), scale=1)
    print('rotation matrix:')
    print(R)
    print()
    img2 = cv2.warpAffine(img, R, dsize=(width, height), borderValue=(114, 114, 114))

    cv2.imshow('raw', img[:, :, ::-1])
    cv2.imshow('rotate', img2[:, :, ::-1])
    cv2.moveWindow('raw', 50, 250)
    cv2.moveWindow('rotate', 700, 250)
    key = cv2.waitKey()
    if key == 27:
        break
cv2.destroyAllWindows()
