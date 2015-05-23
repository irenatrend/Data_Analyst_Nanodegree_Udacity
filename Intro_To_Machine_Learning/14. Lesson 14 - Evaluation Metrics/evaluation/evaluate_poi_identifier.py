#!/usr/bin/python

"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../../final_project/final_project_dataset.pkl", "r"))

# add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

# your code goes here

# Splitting train/test
from sklearn.cross_validation import train_test_split
train_features, test_features, train_labels, test_labels = train_test_split(features, labels,
                                                                            test_size=0.3, random_state=42)

# Train decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

clf = DecisionTreeClassifier()
clf.fit(train_features, train_labels)
clf.score(test_features, test_labels)

# How many POIs are predicted for the test set for your POI identifier?
print "How many POIs are predicted for the test set for your POI identifier?"
print clf.predict(test_features)

import numpy as np
print np.array(test_labels)
print len([e for e in test_labels if e == 1.0])

# Number of People in Test Set
print "Number of People in Test Set:", len(test_labels)

# If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
print 1. - (5./29.)

# Do you get any true positives?
# (In this case, we define a true positive as a case where both the actual label and the predicted label are 1)

# What is the precision?
print "What is the precision?"
from sklearn.metrics import *
print precision_score(test_labels, clf.predict(test_features))


# What is the recall?
print "What is the recall?"
print recall_score(test_labels, clf.predict(test_features))


# How many true positives are there?
print "How many true positives are there?"

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

# What's the precision of this classifier?
print precision_score(true_labels, predictions)

# What's the recall of this classifier?
print recall_score(true_labels,predictions)




#print "Confusion Matrix:\n", confusion_matrix(test_labels, pred), "\n"
#print "Classification Report:\n", classification_report(test_labels, pred)
#print "Accuracy:", accuracy_score(test_labels, pred)


