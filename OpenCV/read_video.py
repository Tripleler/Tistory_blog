import os
import sys
import cv2

cap = cv2.VideoCapture('../sample_num/7.mp4')

if not cap.isOpened():
    print("Video open failed!")
    sys.exit()

print('Frame width:', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('FPS:', round(cap.get(cv2.CAP_PROP_FPS)))
print('Frame count:', round(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
i = 0
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
    i += 1
    if i == 10:
        os.rename("../sample_num/7.mp4", "../sample_num/77.mp4")
        # os.remove("../sample_num/7.mp4")
cap.release()
cv2.destroyAllWindows()
