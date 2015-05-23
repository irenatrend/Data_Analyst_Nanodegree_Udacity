__author__ = 'irenat'

# RandomizedPCA(copy=True, iterated_power=3, n_components=2, random_state=None, whiten=False)

import numpy as np
from sklearn.decomposition import RandomizedPCA

print "--------------------------"
print "PCA"
# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
X = np.array([[-1, -1, 1], [-2, -1, 2], [-3, -2, 2], [1, 1, 1], [2, 1, 1], [3, 2, 0]])

# Principal component analysis (PCA) using randomized SVD
# Linear dimensionality reduction using approximated Singular Value Decomposition
# # of the data and keeping only the most significant singular vectors to project
# the data to a lower dimensional space.

pca = RandomizedPCA(n_components=3)
pca.fit(X)

print "explained_variance_ratio_"
print (pca.explained_variance_ratio_)
print "components_"
print (pca.components_)
print "mean_"
print (pca.mean_)

X_train_pca = pca.transform(X)


# n_components
# Maximum number of components to keep. When not given or None, this is set to n_features (the second dimension of the training data).

# transform(X[, y]) Apply dimensionality reduction on X.
# X is projected on the first principal components previous extracted from a training set.

print "--------------------------"
print "SCALING"

print("SCALE")
from sklearn import preprocessing
import numpy as np
X = np.array([[1., -1.,  2.], [2.,  0.,  0.], [0.,  1., -1.]])

print "X:"
print X
X_scaled = preprocessing.scale(X)
print "X_scaled:"
print X_scaled
print "X_scaled.mean:"
print X_scaled.mean(axis=0)
print "X_scaled.std:"
print X_scaled.std(axis=0)

print "--------------------------"
print "StandardScaler"

scaler = preprocessing.StandardScaler().fit(X)
print "Scaled:"
print scaler
print "scaler.mean"
print scaler.mean_
print "scaler.std"
print scaler.std_

print "scaler.transform"
print scaler.transform(X)

print "scaler.transform([[-1.,  1., 0.]])"
print scaler.transform([[-1.,  1., 0.]])

print "--------------------------"
print "MinMaxScaler"

X_train = np.array([[1., -1.,  2.], [2.,  0.,  0.], [0.,  1., -1.]])
print "X_train:"
print X_train

min_max_scaler = preprocessing.MinMaxScaler()

X_train_minmax = min_max_scaler.fit_transform(X_train)
print "X_train_minmax:"
print X_train_minmax

X_test = np.array([[-3., -1.,  4.]])
X_test_minmax = min_max_scaler.transform(X_test)

print "X_test_minmax:"
print X_test_minmax

print "min_max_scaler.scale_: ", min_max_scaler.scale_
print "min_max_scaler.min_: ", min_max_scaler.min_

