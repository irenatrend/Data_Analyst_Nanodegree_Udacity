#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../../final_project/final_project_dataset.pkl", "r") )

# add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


# it is all yours from here forward!
from sklearn import tree

# Question 1 - what is the accuracy?
clf1 = tree.DecisionTreeClassifier()
clf1 = clf1.fit(features, labels)
print "Accuracy 1:", clf1.score(features, labels)

# Accuracy: 0.989583333333
#  THIS IS AN OVERFIT TREE, DO NOT TRUST THIS NUMBER!
# Pretty high accuracy, huh? Yet another case where testing on the training
# data would make you think you were doing amazingly well,
# but as you already know, that is exactly what holdout test data is for...


# Question 2 - what is the accuracy?
from sklearn import cross_validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

clf2 = tree.DecisionTreeClassifier()
lf = clf2.fit(X_train, y_train)
print "Accuracy 2:", clf2.score(X_test, y_test)

# And the testing data brings us back down to earth
# after that 99% accuracy in the last quiz.


