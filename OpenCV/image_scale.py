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

# parameter
scale = 0.1

while True:
    # Random scale
    s = random.uniform(1 - scale, 1 + scale)

    S = cv2.getRotationMatrix2D(angle=0, center=center, scale=s)
    img2 = cv2.warpAffine(img, S, dsize=(width, height), borderValue=(114, 114, 114))

    # 2-1 Fixed scale
    # scale = 0.5
    #
    # T1 = np.eye(3)
    # T1[0, 2], T1[1, 2] = center
    #
    # T2 = np.eye(3)
    # T2[0, 2], T2[1, 2] = -center[0], -center[1]
    #
    # S = np.eye(3)
    # S[0, 0] = scale
    # S[1, 1] = scale
    #
    # A = T1 @ S @ T2
    # img2 = cv2.warpAffine(img, A[:2], dsize=(width, height), borderValue=(114, 114, 114))

    # 2-2 Random scale with free shape
    # T1 = np.eye(3)
    # T1[0, 2], T1[1, 2] = center
    #
    # T2 = np.eye(3)
    # T2[0, 2], T2[1, 2] = -center[0], -center[1]
    #
    # S = np.eye(3)
    # S[0, 0] = random.uniform(0.1, 1)
    # S[1, 1] = random.uniform(0.1, 1)
    #
    # A = T1 @ S @ T2
    # img2 = cv2.warpAffine(img, A[:2], dsize=(width, height), borderValue=(114, 114, 114))

    cv2.imshow('Raw', img[:, :, ::-1])
    cv2.imshow('Scale', img2[:, :, ::-1])
    cv2.moveWindow('Raw', 50, 250)
    cv2.moveWindow('Scale', 700, 250)

    key = cv2.waitKey()
    if key == 27:
        break
cv2.destroyAllWindows()
