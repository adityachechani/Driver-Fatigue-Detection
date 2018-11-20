# import necessary packages
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2

def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    return (x, y, w, h)

def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)

    for i in range(68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords

def checkYawn(shape, count):
    diff = shape[67][1] - shape[63][1]
    
    if diff > 7:
        count += 1
    else:   
        count = 0
        return (False, count)

    if count >= 20:
        return (True, count)

    return (False, count)

def checkGaze(shape):
    return abs(abs(shape[34][0] - shape[3][0]) - abs(shape[34][0] - shape[15][0]))


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")

cam = cv2.VideoCapture(0)
count = 1

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 1)

    # for i, rect in enumerate(rects):
    if len(rects) > 0:
        shape = predictor(gray, rects[0])
        shape = shape_to_np(shape)

        (x, y, w, h) = rect_to_bb(rects[0])

        cv2.putText(frame, "Face #{}".format(1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        eye1 = frame[shape[18][1]:shape[29][1], shape[18][0]:shape[29][0]] # // 3].astype('uint8')
        eye1 = cv2.resize(eye1, (200, 200))        
        
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

        state, count = checkYawn(shape, count)
        gaze = checkGaze(shape)

        if gaze > 30:
            print("gaze Off")

        # if state:
        #     print("Driver drowsy")
        
        cv2.imshow("eye1", eye1)
    k = cv2.waitKey(1)
    
    if k%256 == 27:
        # print(converted.shape[0])
        # ESC pressed
        print("Escape hit, closing...")
        break
    # cv2.destroyAllWindows()
    cv2.imshow("test", frame)



cv2.destroyAllWindows()