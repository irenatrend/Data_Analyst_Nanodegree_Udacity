#!/usr/bin/python

"""
    starter code for the regression mini-project
    
    loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project)

    draws a little scatterplot of the training/testing data

    you fill in the regression code where indicated

"""    


import sys
import pickle
sys.path.append("../../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load(open("../../final_project/final_project_dataset_modified.pkl", "r"))

# list the features you want to look at--first item in the
# list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat(dictionary, features_list, remove_any_zeroes=True)  # "long_term_incentive"], remove_any_zeroes=True )
target, features = targetFeatureSplit(data)

# training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"

# your regression goes here!
# please name it reg, so that the plotting code below picks it up and
# plots it correctly

from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(feature_train, target_train)
pred = reg.predict(feature_test)

print "Slope:", reg.coef_
print "Intercept:", reg.intercept_

# What is the score of the regression on the training data?
print reg.score(feature_train, target_train)

# What is that score on the testing data?
print reg.score(feature_test, target_test)


# We have a better score when using long-term incentive to predict someones bonus, which translates to a better fit.
# salary -1.48499241737
# long_term_incentive -0.59271289995

# draw the scatterplot,with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter(feature, target, color=test_color)
for feature, target in zip(feature_train, target_train):
    plt.scatter(feature, target, color=train_color)

# labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")


# draw the regression line, once it's coded
try:
    plt.plot(feature_test, reg.predict(feature_test))
except NameError:
    pass
plt.xlabel(features_list[1])

reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="r")

print "Slope:", reg.coef_
# The slope is about 2.27 after removing the outlier, which is a big difference
# from what we had before (about 5.4).
# A small number of outliers makes a big difference!

plt.ylabel(features_list[0])
plt.legend()
plt.show()

# references
# http://scikit-learn.org/stable/modules/linear_model.html
# http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#example-linear-model-plot-ols-py
