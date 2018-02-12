import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global  clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

# 启动摄像头
cameraCapure = cv2.VideoCapture(0)
cv2.namedWindow('camera')
cv2.setMouseCallback('camera',onMouse)

print('any key stop')

success, frame = cameraCapure.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('camera', frame)
    success, frame = cameraCapure.read()

cv2.destroyWindow('camera')
cameraCapure.release()