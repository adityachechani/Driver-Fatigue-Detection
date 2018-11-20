import os
import numpy as np
import random
import cv2

path = "facial_landmark_data"

def create_dir(folder):
	try:
		os.makedirs(folder)
	except:
		print("{} already exists".format(folder))

def drawRectangle(img, bbox):
	x1, y1, x2, y2 = bbox
	cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), thickness=5, lineType=cv2.LINE_8)

def drawLandmarks(img, parts):
	for i, part in enumerate(parts):
		px, py = part
		cv2.circle(img, (px, py), 1, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
		cv2.putText(img, str(i+1), (px, py), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 100), 4)

scale = 4
num_samples = 50

fldDir = path
numPoints = 70

outputDir = os.path.join(fldDir, "samples")
outputMirrorDir = os.path.join(outputDir, "mirror")
outputOriginalDir = os.path.join(outputDir, "original")
create_dir(outputMirrorDir)
create_dir(outputOriginalDir)

imgNamesFilepath = os.path.join(fldDir, "image_names.txt")

if os.path.exists(imgNamesFilepath):
	with open(imgNamesFilepath) as f:
		imgNames = [x.strip() for x in f.readlines()]
else:
	print("Cannot get image file names")

random.shuffle(imgNames)
imgNamesSampled = imgNames[:num_samples]

for k, imageName in enumerate(imgNamesSampled):
	print("processing file: {}".format(imageName))
	imPath = os.path.join(fldDir, imageName)
	im = cv2.imread(imPath, cv2.IMREAD_COLOR)
	im = cv2.resize(im, (0, 0), fx=scale, fy=scale)

	rectPath = os.path.splitext(imPath)[0] + "_rect.txt"

	with open(rectPath) as f:
		line = f.readline()
	left, top, width, height = [float(l) for l in line.strip().split()]
	right = left + width
	bottom = top + height

	x1, y1, x2, y2 = int(left*scale), int(top*scale), int(right*scale), int(bottom*scale)
	bbox = [x1, y1, x2, y2]

	dataPath = os.path.splitext(imPath)[0] + "_bv" + str(numPoints) + ".txt"
	parts = []
	with open(dataPath) as f:
		lines = [l.strip() for l in f.readlines()]

	for line in lines:
		x, y = [float(n) for n in line.split()]
		px, py = int(x * scale), int(y * scale)
		parts.append([px, py])

	drawRectangle(im, bbox)
	drawLandmarks(im, parts)

	imageBaseName = os.path.basename(imPath)
	if 'mirror' in imageBaseName:
		outputImagePath = os.path.join(outputMirrorDir, imageBaseName)
	else:
		outputImagePath = os.path.join(outputOriginalDir, imageBaseName)

	# save output image
	cv2.imwrite(outputImagePath, im)

