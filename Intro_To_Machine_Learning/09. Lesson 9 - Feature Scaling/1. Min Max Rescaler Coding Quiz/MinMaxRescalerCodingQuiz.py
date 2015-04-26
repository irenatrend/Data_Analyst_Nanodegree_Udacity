""" quiz materials for feature scaling clustering """

# FYI, the most straightforward implementation might
# throw a divide-by-zero error, if the min and max
# values are the same
# but think about this for a second--that means that every
# data point has the same value for that feature!
# why would you rescale it?  Or even use it at all?


def featureScaling(arr):

    # Solution 1
    # fs = []
    # for item in arr:
    #    pitem = (item - min(arr))/float((max(arr) - min(arr)))
    #    fs.append(pitem)

    # Solution 2
    from sklearn.preprocessing import MinMaxScaler
    import numpy
    fs = []
    for item in arr:
        fs.append(float(item))

    scaler = MinMaxScaler()
    w = numpy.array(fs)
    fs = scaler.fit_transform(w)

    return fs

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)

# References
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html
# http://scikit-learn.org/stable/modules/preprocessing.html
