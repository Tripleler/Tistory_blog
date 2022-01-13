import sys
import cv2

img = cv2.imread('../icon/logo.png')
if img is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('gray', dst)

cv2.resizeWindow('img', 500, 500)
cv2.moveWindow('img', 15, 15)
cv2.moveWindow('gray', 600, 15)

img2 = cv2.resize(img, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
cv2.imshow('resize', img2)
cv2.moveWindow('resize', 150, 600)

cv2.waitKey()
cv2.destroyAllWindows()