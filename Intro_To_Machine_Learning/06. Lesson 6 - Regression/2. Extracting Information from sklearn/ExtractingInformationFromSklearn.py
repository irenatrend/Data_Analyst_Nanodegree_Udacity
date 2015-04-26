# import LinearRegression, create regression (name it reg)
# and fit it to the training data

from sklearn.linear_model import LinearRegression
reg = LinearRegression()

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

reg.fit(age_train, net_worths_train)


print "katie's net worth prediction: ", reg.predict([27])
print "slope", reg.coef_
print "intercept:", reg.intercept_

print "\n ###### stats on test dataset ##### \n"
print "r-scored score:", reg.score(ages_test, net_worths_test)

print "\n ###### stats on training dataset ##### \n"
print "r-scored score:", reg.score(ages_train, net_worths_train)

import matplotlib.pyplot as plt
plt.scatter(ages, net_worth)
plt.plot(ages, reg.predict(ages), color='blue', linewidth=3)
plt.xlabel("ages")
plt.ylabel("net worths")
plt.show()