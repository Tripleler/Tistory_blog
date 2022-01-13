import sys
import cv2

cap = cv2.VideoCapture('../sample_num/7.mp4')

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

print('Frame width:', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('FPS:', round(cap.get(cv2.CAP_PROP_FPS)))
print('Frame count:', round(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

while True:

    ret, frame = cap.read()
    print(ret)
    if not ret:
        break

    print('Prop pos frames:', round(cap.get(cv2.CAP_PROP_POS_FRAMES)))

    cv2.imshow('frame', frame)

    delay = 1

    if cv2.waitKey(delay) == 27:
        break

cap.release()
cv2.destroyAllWindows()