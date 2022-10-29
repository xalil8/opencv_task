import cv2
import math
import numpy as np 

import os


new_list = []
for i in os.listdir("saved"):
    if i ==".DS_Store":
        continue
    a = "saved/" + i
    new_list.append(a)

#new_list.remove(".DS_Store")
frames  = sorted(new_list)





fps = 10
width = 540
height = 300
output_size = (width, height)
out = cv2.VideoWriter("xalil.mp4",cv2.VideoWriter_fourcc('M','J','P','G'), fps , output_size )

for i in frames:    
    frame = cv2.imread(i)
    cv2.imshow('Video Frame', frame)
    out.write(cv2.resize(frame, output_size ))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
cv2.destroyAllWindows()
