import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, im = cap.read()
    cv2.imshow('video test', im)
    key = cv2.waitKey(10)
    if key == 27:# esc
         break
    if key == ord(' '): # 空格
         cv2.imwrite('vid_result.jpg',im)