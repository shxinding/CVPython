import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, im = cap.read()
    blur = cv2.GaussianBlur(im, (0,0), 5)
    cv2.imshow('camera', blur)
    if cv2.waitKey(10) == 27:
        break