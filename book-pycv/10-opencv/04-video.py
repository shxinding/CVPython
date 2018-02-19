import cv2
from numpy import *

cap = cv2.VideoCapture(0)
frames = []

while True:
    ret, im = cap.read()
    cv2.imshow('video', im)
    frames.append(im)
    if cv2.waitKey(10) == 27:
        break

frames = array(frames)
print(im.shape)
print(frames.shape)