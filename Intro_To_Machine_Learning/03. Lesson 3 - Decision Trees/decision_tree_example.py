#from sklearn import tree
#X = [[0, 0], [1, 1]]
#Y = [0, 1]
#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X, Y)

#print(clf.predict([[2., 2.]]))

##############################

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf1 = tree.DecisionTreeClassifier()
clf1 = clf1.fit(iris.data, iris.target)

print(clf1.predict([[2., 2.]]))