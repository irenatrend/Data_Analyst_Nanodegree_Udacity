#!/usr/bin/python 

""" 
    skeleton code for k-means clustering mini-project

"""

import pickle
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../../tools/")
from feature_format import featureFormat, targetFeatureSplit


def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    # plot each cluster with a different color--add more colors for
    # drawing more than 4 clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    # if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()

# load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load(open("../../final_project/final_project_dataset.pkl", "r"))
# there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

# Stock Option and Salary Range Quiz
max_exercised_stock_options = \
    max(v['exercised_stock_options']
        for (k, v) in data_dict.iteritems()
        if not math.isnan(float(v['exercised_stock_options'])))
min_exercised_stock_options = \
    min(v['exercised_stock_options']
        for (k, v) in data_dict.iteritems()
        if not math.isnan(float(v['exercised_stock_options'])))
max_salary = max(v['salary'] for (k, v) in data_dict.iteritems() if not math.isnan(float(v['salary'])))
min_salary = min(v['salary'] for (k, v) in data_dict.iteritems() if not math.isnan(float(v['salary'])))

print "Max Exercised Stock Options:", max_exercised_stock_options
print "Min Exercised Stock Options:", min_exercised_stock_options
print "Max Salary:", max_salary
print "Min Salary:", min_salary


# import pprint
# pp = pprint.PrettyPrinter(depth = 6)
# pp.pprint(data_dict)


# the input features we want to use
# can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit(data)


# in the "clustering with 3 features" part of the mini-project,
# you'll want to change this line to
# for f1, f2, _ in finance_features:
# (as it's currently written, line below assumes 2 features)
for f1, f2, f3 in finance_features:
    plt.scatter(f1, f2)
plt.show()



from sklearn.cluster import KMeans

features_list = ["poi", feature_1, feature_2, feature_3]
data2 = featureFormat(data_dict, features_list)
poi, finance_features = targetFeatureSplit(data2)
clf = KMeans(n_clusters=2)
pred = clf.fit_predict(finance_features)
Draw(pred, finance_features, poi, name="clusters_before_scaling.pdf", f1_name=feature_1, f2_name=feature_2)


# cluster here; create predictions of the cluster labels
# for the data and store them to a list called pred
pred = clf.predict(finance_features)





try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"


# References
# http://scikit-learn.org/stable/modules/clustering.html



