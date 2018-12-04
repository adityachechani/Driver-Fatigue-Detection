import os
import sys
import dlib
import random
from lxml import etree as ET


def createXML(imageNames, xmlFileName, numPoints):
    dataset = ET.Element("dataset")
    ET.SubElement(dataset, "name").text = "Training Faces"
    images = ET.SubElement(dataset, "images")
    numFiles = len(imageNames)

    print("{0} : {1} files".format(xmlFileName, numFiles))

    for k,imgName in enumerate(imageNames):
        print("{}:{} - {}".format(k+1, numFiles, imgName))
        rectName = os.path.splitext(imgName)[0] + "_rect.txt"
        with open(os.path.join(fldDataDir, rectName), 'r') as file:
            rect = file.readline()
        rect = rect.split()
        left, top, width, height = rect

        image = ET.SubElement(images, "image", file=imgName)
        box = ET.SubElement(image, "box", top=top, left=left, width=width, height=height)

        points_name = os.path.splitext(imgName)[0] + "_bv" + str(numPoints) + ".txt"
        with open(os.path.join(fldDataDir, points_name), 'r') as file:
            for i, point in enumerate(file):
                x, y = point.split()
                x = str(int(float(x)))
                y = str(int(float(y)))
                name = str(i).zfill(2)

                ET.SubElement(box, 'part', name=name, x=x, y=y)


    tree = ET.ElementTree(dataset)
    print("writing on disk: {}".format(xmlFileName))
    tree.write(xmlFileName, pretty_print=True, xml_declaration=True, encoding="UTF-8")


if __name__ == '__main__':
    fldDataDir = "facial_landmark_data"
    numPoints = 70

    with open(os.path.join(fldDataDir, "image_names.txt")) as f:
        imageNames = [x.strip() for x in f.readlines()]


    # n = 1000
    # imageNames = random.sample(imageNames, n)
    
    totalNumFiles = len(imageNames)
    numTestFiles = int(0.05 * totalNumFiles)

    testFiles = random.sample(imageNames, numTestFiles)
    trainFiles = list(set(imageNames) - set(testFiles))

    xmlTrainPathFile = os.path.join(fldDataDir, "train_face_landmarks_70.xml")
    xmlTestPathFile = os.path.join(fldDataDir, "test_face_landmarks_70.xml")
    numPoints = 70

    createXML(trainFiles, xmlTrainPathFile, numPoints)
    createXML(testFiles, xmlTestPathFile, numPoints)
