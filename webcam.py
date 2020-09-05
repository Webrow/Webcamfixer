import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

points = []

def onMouse(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        if len(points) < 5:
            tmp = []
            tmp.append(x)
            tmp.append(y)
            print("printing point:", x, y)
            points.append(tmp)
            if len(points) == 4:
                getPers()


M = False

def getPers():
    global M
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[768,0],[0,432],[768,432]])
    M = cv2.getPerspectiveTransform(pts1, pts2)


while(True):

    if len(points) < 4:
        # Capture frame-by-frame
        ret, frame = cap.read()
        cv2.setMouseCallback('frame', onMouse)

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)

    if len(points) > 3:
        ret, frame = cap.read()
        
        dst = cv2.warpPerspective(frame, M, (768,432))

        cv2.imshow('frame', dst)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
