#!/usr/bin/python

import matplotlib.pyplot as plt
import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat
from feature_format import targetFeatureSplit

from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import RandomizedPCA
from sklearn.pipeline import Pipeline

import helper

# Step 1: Select features
# features_list is a list of strings, each of which is a feature name
# first feature must be "poi", as this will be singled out as the label
target_label = 'poi'
email_features_list = [
    # 'email_address', # informational label
    'from_messages',
    'from_poi_to_this_person', 'from_this_person_to_poi',
    'shared_receipt_with_poi', 'to_messages']

financial_features_list = [
    'bonus', 'deferral_payments', 'deferred_income', 'director_fees', 'exercised_stock_options', 'expenses',
    'loan_advances', 'long_term_incentive', 'other', 'restricted_stock', 'restricted_stock_deferred',
    'salary', 'total_payments', 'total_stock_value']

features_list = ['poi'] + financial_features_list + email_features_list

# load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r"))


# Step 2: Remove outliers
# helper.plot_salary_bonus(data_dict)
data_dict.pop('TOTAL', 0)
# helper.plot_salary_bonus(data_dict)

# Step 3: Create new features and select final feature list (feature_list)
# store to my_dataset for easy export below
my_dataset = data_dict

for name in my_dataset:
    data_point = my_dataset[name]

    data_point["emails_fraction_from_poi"] = \
        helper.calculate_fraction(data_point["from_poi_to_this_person"], data_point["to_messages"])

    data_point["emails_fraction_to_poi"] = \
        helper.calculate_fraction(data_point["from_this_person_to_poi"], data_point["from_messages"])

# Get K-best features
num_features = 10
k_best_features = helper.get_kbest(data_dict, features_list, num_features)
# features_list = ['poi'] + k_best_features.keys()

features_list = ['poi'] + ['exercised_stock_options', 'total_stock_value', 'bonus', 'salary']

# Get features importance
# helper.get_features_ranking(data_dict, features_list)

# these two lines extract the features specified in features_list
# and extract them from data_dict, returning a numpy array
data = featureFormat(my_dataset, features_list)

# split into labels and features (this line assumes that the first
# feature in the array is the label, which is why "poi" must always
# be first in features_list
labels, features = targetFeatureSplit(data)

# Step 4: Try a different classifiers, and choose one final
scaler = StandardScaler()
pca = RandomizedPCA(n_components=2, copy=True, whiten=False)
clf = DecisionTreeClassifier(min_samples_split=2, random_state=10)

estimator = [('scaler', scaler), ('reduce_dim', pca), ('tree', clf)]

clf = Pipeline(estimator)


# RandomForestClassifier
# from sklearn import ensemble
# clf = ensemble.RandomForestClassifier(criterion='gini', n_estimators=14, max_depth=7,
#                                      max_features=None, random_state=42, min_samples_split=1)


# Step 5: Tune classifier using GridSearchCV
# from sklearn.grid_search import GridSearchCV
# params = dict(reduce_dim__n_components=[1, 2, 3], tree__min_samples_split=[2, 4, 6, 8 10])
# clf = GridSearchCV(clf, param_grid=params, n_jobs=-1, scoring='recall')


# dump your classifier, dataset and features_list so
# anyone can run/check your results
pickle.dump(clf, open("my_classifier.pkl", "w"))
pickle.dump(data_dict, open("my_dataset.pkl", "w"))
pickle.dump(features_list, open("my_feature_list.pkl", "w"))