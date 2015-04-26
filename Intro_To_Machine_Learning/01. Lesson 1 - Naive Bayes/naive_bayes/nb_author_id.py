#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project 

    use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time

sys.path.append("../../tools/")
from email_preprocess import preprocess

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
# your code goes here

clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
predict = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

# compare the predicted label value with the actual label value
accuracy = accuracy_score(labels_test, predict)
print "accuracy:", accuracy

#########################################################

# references
# https://piazza.com/class/i23uptiifb6194?cid=119
# http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html