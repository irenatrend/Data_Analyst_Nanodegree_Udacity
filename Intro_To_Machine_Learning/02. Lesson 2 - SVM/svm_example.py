from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]

clf = svm.SVC()
clf.fit(X, y)

print(clf.predict([[2., 2.]]))

# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
# gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
# shrinking=True, tol=0.001, verbose=False)

# take as input two arrays:
# an array X of size [n_samples, n_features] holding the training samples
# and an array y of class labels (strings or integers)
# size [n_samples]


# the labels are outputs when testing, or making predictions.
# When you're training, of course you need to provide the labels to the
# algorithm to help it figure out the patterns, which might make the labels sound like inputs in a way.