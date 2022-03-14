import sys
import cv2
import math
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

shear = 0

while True:
    # scale
    R = np.eye(3)
    R[:2] = cv2.getRotationMatrix2D(angle=0, center=(width / 2, height / 2), scale=0.5)

    # Shear
    S = np.eye(3)
    S[0, 1] = math.tan(shear * math.pi / 180)  # x shear (deg)
    S[1, 0] = math.tan(shear * math.pi / 180)  # y shear (deg)
    shear += 1

    M = S @ R
    img2 = cv2.warpAffine(img, M[:2], dsize=(width, height), borderValue=(114, 114, 114))

    cv2.imshow('raw', img[:, :, ::-1])
    cv2.imshow('shear', img2[:, :, ::-1])
    cv2.moveWindow('raw', 50, 250)
    cv2.moveWindow('shear', 700, 250)

    key = cv2.waitKey()
    if key == 27:
        break
cv2.destroyAllWindows()
