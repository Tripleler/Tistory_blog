import sys
import cv2
import numpy as np

img = cv2.imread('../icon/flowers.jpg')
img = cv2.resize(img, (480, 320))

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('raw_img', img)
cv2.moveWindow('raw_img', 100, 100)

val = 0
mask = np.full((320, 480, 3), (val, val, val)).astype(np.uint8)

while True:
    mask = np.full((320, 480, 3), (val, val, val)).astype(np.uint8)

    lightness = cv2.add(img, mask)
    cv2.imshow('light_img', lightness)
    cv2.moveWindow('light_img', 580, 100)

    darkness = cv2.subtract(img, mask)
    cv2.imshow('dark_img', darkness)
    cv2.moveWindow('dark_img', 1060, 100)

    key = cv2.waitKey()
    if key == 27:
        break
    if key == ord('u'):
        val += 5
    if key == ord('d'):
        val -= 5
cv2.destroyAllWindows()




cv2.waitKey()
cv2.destroyAllWindows()
