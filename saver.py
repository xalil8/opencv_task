import cv2
import os

count=1


vidcap = cv2.VideoCapture("video.mp4")
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("C:/Users/halil/Desktop/opencv_task"+str(count)+".jpg", image) # Save frame as JPG file
  
    sec = 0
    frameRate = 0.5 # Change this number to 1 for each 1 second
    
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)

print("worked")