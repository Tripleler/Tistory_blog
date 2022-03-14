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

# parameter
translate = 0.5

while True:
    # Random translation
    T = np.eye(3)
    T[0, 2] = random.uniform(-translate, translate) * width  # x translation (pixels)
    T[1, 2] = random.uniform(-translate, translate) * height  # y translation (pixels)

    # Fixed translation
    # T[0, 2] = translate * width  # x translation (pixels)
    # T[1, 2] = translate * height  # y translation (pixels)

    img2 = cv2.warpAffine(img, T[:2], dsize=(width, height), borderValue=(114, 114, 114))

    cv2.imshow('Raw', img[:, :, ::-1])
    cv2.imshow('Translate', img2[:, :, ::-1])
    cv2.moveWindow('Raw', 50, 250)
    cv2.moveWindow('Translate', 700, 250)

    key = cv2.waitKey()
    if key == 27:
        break
cv2.destroyAllWindows()
