import os
import dlib

fldDataDir = "facial_landmark_data"
numPoints = 70
modelName = "predictor_" + str(numPoints) + "_face_landmarks.dat"

options = dlib.shape_predictor_training_options()
options.cascade_depth = 10
options.num_trees_per_cascade_level = 500
options.tree_depth = 4
options.nu = 0.1
options.oversampling_amount = 20
options.feature_pool_size = 400
options.feature_pool_region_padding = 0
options.lambda_param = 0.1
options.num_test_splits = 20

options.be_verbose = True

trainingXMLPath = os.path.join(fldDataDir, "train_face_landmarks_70.xml")
testingXMLPath = os.path.join(fldDataDir, "test_face_landmarks_70.xml")

outputModelPath = os.path.join(fldDataDir, modelName)
print("entering")
if(os.path.exists(trainingXMLPath) and os.path.exists(testingXMLPath)):
    dlib.train_shape_predictor(trainingXMLPath, outputModelPath, options)

    print("\nTraining Accuracy: {}".format(dlib.test_shape_predictor(trainingXMLPath, outputModelPath)))
    print("\nTesting Accuracy: {}".format(dlib.test_shape_predictor(testingXMLPath, outputModelPath)))

else:
  print('training and test XML files not found.')
  print('Please check paths:')
  print('train: {}'.format(trainingXmlPath))
  print('test: {}'.format(testingXmlPath))