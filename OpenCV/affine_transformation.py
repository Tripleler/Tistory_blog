import sys
import cv2
import math
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

# Parameter
degrees = 30
scale = 0.2
shear = 30
translate = 0.2
flip_ud = 0.5
flip_lr = 0.5

while True:
    # Center
    T1 = np.eye(3)
    T1[0, 2], T1[1, 2] = center

    T2 = np.eye(3)
    T2[0, 2], T2[1, 2] = -center[0], -center[1]

    # Rotation
    r = random.uniform(-degrees, degrees)
    R = np.eye(3)
    R[:2] = cv2.getRotationMatrix2D(angle=r, center=center, scale=1)

    # Shear
    S = np.eye(3)
    S[0, 1] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # x shear (deg)
    S[1, 0] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # y shear (deg)

    # Translation
    T = np.eye(3)
    T[0, 2] = random.uniform(-translate, translate) * width  # x translation (pixels)
    T[1, 2] = random.uniform(-translate, translate) * height  # y translation (pixels)

    # Scale
    SC = np.eye(3)
    SC[0, 0] = random.uniform(0.5-scale, 0.5+scale)
    SC[1, 1] = random.uniform(0.5-scale, 0.5+scale)

    # Flip
    UD = np.eye(3)
    UD[1, 1] = -1 if random.uniform(0, 1) > flip_ud else 1

    LR = np.eye(3)
    LR[0, 0] = -1 if random.uniform(0, 1) > flip_lr else 1

    # Define Affine Matrix A
    A = T1 @ T @ S @ R @ SC @ T2
    img2 = cv2.warpAffine(img, A[:2], dsize=(width, height), borderValue=(114, 114, 114))

    cv2.imshow('raw', img[:, :, ::-1])
    cv2.imshow('affine', img2[:, :, ::-1])
    cv2.moveWindow('raw', 50, 250)
    cv2.moveWindow('affine', 700, 250)

    key = cv2.waitKey()
    if key == 27:
        break
cv2.destroyAllWindows()
