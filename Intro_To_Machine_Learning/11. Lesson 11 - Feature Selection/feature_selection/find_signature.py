#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


# the words (features) and authors (labels), already largely processed
words_file = "word_data_overfit.pkl"  # like the file you made in the last mini-project
authors_file = "email_authors_overfit.pkl"  # this too
word_data = pickle.load(open(words_file, "r"))
authors = pickle.load(open(authors_file, "r"))


# test_size is the percentage of events assigned to the test set (remainder go into training)
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = \
    cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train).toarray()
features_test = vectorizer.transform(features_test).toarray()


# a classic way to overfit is to use a small number
# of data points and a large number of features
# train on only 150 events to put ourselves in this regime
features_train = features_train[:150]
labels_train = labels_train[:150]


# your code goes here

# What is the accuracy of the decision tree you just made?
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print "Accuracy:", clf.score(features_test, labels_test)


# What is the importance of the most important feature? What is the number of this feature?
import numpy as np
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
print 'Feature Ranking: '
for i in range(10):
    print "{} feature no.{} ({})".format(i+1, indices[i], importances[indices[i]])  # feature no.33614 (0.764705882353)


# What is the most powerful word when your decision tree is making its classification decisions?

print vectorizer.get_feature_names()[33604]  # 'sshacklensf'
