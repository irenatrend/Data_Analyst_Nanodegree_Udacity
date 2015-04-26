import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from time import time

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

########################## SVM #################################
# we handle the import statement and SVC creation for you here
from sklearn.svm import SVC
clf = SVC(kernel="linear")

# now your job is to fit the classifier
# using the training features/labels, and to
# make a set of predictions on the test data
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() - t0, 3), "s"

# store your predictions in a list named pred
t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time() - t1, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

def submitAccuracy():
    return acc