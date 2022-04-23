import sys
import cv2

cap = cv2.VideoCapture('md.mp4')

if not cap.isOpened():
    print("Video open failed!")
    sys.exit()

fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS:', fps)
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Frame width:', w)
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame height:', h)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    f = round(cap.get(cv2.CAP_PROP_POS_FRAMES))
    print('Prop pos frames:', f)

    cv2.imshow('frame', frame)
    cv2.moveWindow('frame', 300, 100)

    key = cv2.waitKey()

    if key == 27:
        break
    if key == ord('b'):
        cap.set(cv2.CAP_PROP_POS_FRAMES, f - 2)

cap.release()
cv2.destroyAllWindows()

# cap = cv2.VideoCapture('Raw.mp4')
# out = cv2.VideoWriter('Cut.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
# cap.set(cv2.CAP_PROP_POS_FRAMES, 116)
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     out.write(frame)
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()
#
# print('Edit Finished')
