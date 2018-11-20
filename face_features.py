import dlib, cv2
import numpy as np
from renderFace import renderFace
from renderFace import renderFace2

# feature_model = "models/shape_predictor_68_face_landmarks.dat"
feature_model = "facial_landmark_data/70_points/shape_predictor_70_face_landmarks.dat"

faceDetector = dlib.get_frontal_face_detector()
landmarkDetector = dlib.shape_predictor(feature_model)
cam = cv2.VideoCapture(0)

cv2.namedWindow("FaceFeatureDetector")

hasFrame, frame = cam.read()
vid_writer = cv2.VideoWriter('output-feature.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (frame.shape[1],frame.shape[0]))

while True:
	ret, frame = cam.read()
	if not ret:
		break

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faceRects = faceDetector(frame, 0)

	landmarksAll = []

	for i in range(0, len(faceRects)):
		newRect = dlib.rectangle(int(faceRects[i].left()), int(faceRects[i].top()), int(faceRects[i].right()), int(faceRects[i].bottom()))

		landmarks = landmarkDetector(gray, newRect)

		renderFace2(frame, landmarks)
	if cv2.waitKey(25) & 0xFF == 27:
		break

	cv2.imshow("FaceFeatureDetector", frame)
	vid_writer.write(frame)
	cv2.waitKey(1)

cv2.destroyAllWindows()	
vid_writer.release()


