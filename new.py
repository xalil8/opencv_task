import cv2
import numpy as np

cap = cv2.VideoCapture('video.mp4')

# (x, y, w, h) = cv2.boundingRect(c)
# cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 20)
# roi = frame[y:y+h, x:x+w]


while True:
    cap = cv2.VideoCapture('video.mp4')
    ret, frame = cap.read()
    # (height, width) = frame.shape[:2]
    my_video = frame[300:750,:]
    cv2.imshow('Video', my_video)


    if cv2.waitKey(28) & 0xFF == ord('q'):
        break


my_video.release()
cv2.destroyAllWindows()