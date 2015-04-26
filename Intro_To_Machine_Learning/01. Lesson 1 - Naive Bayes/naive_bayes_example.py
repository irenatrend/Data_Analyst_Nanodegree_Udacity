import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

# Naive Bayes Example
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()  # create classifier
clf.fit(X, Y)  # fit, train, learn the patterns (X - features, Y - labels)

# We ask the classifier that we just trained, for some predictions,
# We ask what do you think the label is?
# Which class does it belongs to
print(clf.predict([[-0.8, -1]]))

# Result is [1] - belongs to class number 1

# predict(X)	Perform classification on an array of test vectors X.
# Parameters:
# fit(X, y)     Fit Gaussian Naive Bayes according to X, y
# X : array-like, shape = [n_samples, n_features]
#       Training vectors, where n_samples is the number of samples and n_features is the number of features.
# y : array-like, shape = [n_samples]
#      Target values.

# Returns:
# self : object
#       Returns self.