import cv2
import math
import numpy as np 


my_video = cv2.VideoCapture("video.mp4")
new_vid = my_video.get(100)






def  point_transform(frame):
    #corner of the license plate that we wanna get perspective
    #pt1 = left upper, pt2 = right upper, pt2 = left bottom, pt3 = right bottom 
    pt1, pt2, pt3, pt4 = [0,350], [538,300],[10,650],[538,600]
    xf =  abs(pt2[0] - pt1[0])
    yf = abs(pt2[1] - pt1[1])
    width = int(math.sqrt(xf**2 + yf**2))

    x1f =  abs(pt3[1] - pt1[1])
    y1f = abs(pt3[0] - pt1[0])
    height = int(math.sqrt(x1f**2 + y1f**2))

    pts1 = np.float32([pt1, pt2, pt3, pt4])
    pts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgoutput = cv2.warpPerspective(frame, matrix,(width,height))

    return imgoutput

name_count = 0
counter =0
while True:
    _, img = my_video.read()
    


    cropped = point_transform(img)
    cv2.CAP_PROP_POS_MSEC

    #show video, frame by frame 
    if (counter % 3) ==0:
        cv2.imwrite(f"photos/frame{name_count}.jpg", cropped)    
        name_count += 1

    counter += 1



    cv2.imshow("screen", cropped)


    if cv2.waitKey(28) & 0xFF == ord('q'):
        break

#my_video.release()
cv2.destroyAllWindows()