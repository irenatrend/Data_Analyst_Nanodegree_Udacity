import sys
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

sys.path.append("../tools/")

from feature_format import featureFormat
from feature_format import targetFeatureSplit


from sklearn.tree import DecisionTreeClassifier

def plot_salary_bonus(data_dict):
    """
        plot Salary and Bonus
    """

    for point in data_dict:
        salary = data_dict[point]['salary']
        bonus = data_dict[point]['bonus']

        plt.scatter(salary, bonus, c='red' if data_dict[point]['poi'] else 'green', s=40)
        if point == 'TOTAL':
            plt.annotate('Outlier', xy=(salary, bonus), xytext=(-20, 20), textcoords='offset points',
                         ha='right', va='bottom', bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                         arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    plt.xlabel("Salary")
    plt.ylabel("Bonus")

    plt.show()


def calculate_fraction(poi_messages, all_messages):
    """
    return the fraction of messages to/from that person that are from/to a POI
    """

    if poi_messages == 'NaN' or all_messages == 'NaN' or poi_messages == 0 or all_messages == 0:
        fraction = 0.
    else:
        fraction = float(poi_messages) / float(all_messages)

    return fraction


def get_kbest(data_dict, features_list, k):

    """ runs scikit-learn's SelectKBest feature selection
        returns dict where keys=features, values=scores
    """
    data = featureFormat(data_dict, features_list)
    labels, features = targetFeatureSplit(data)

    k_best = SelectKBest(f_classif, k=k)
    k_best.fit(features, labels)
    scores = k_best.scores_

    unsorted_results = zip(features_list[1:], scores)
    sorted_results = list(reversed(sorted(unsorted_results, key=lambda x: x[1])))

    # print sorted_results
    k_best_features = dict(sorted_results[:k])

    print "{0} best features: {1}\n".format(k, k_best_features.keys())
    return k_best_features


def get_features_ranking(data_dict, features_list):

    data = featureFormat(data_dict, features_list)
    labels, features = targetFeatureSplit(data)

    clf = DecisionTreeClassifier()
    clf.fit(features, labels)

    # What is the importance of the most important feature?
    importances = clf.feature_importances_
    print '\nFeature importance from most important to least over entire data set:'
    print [X for Y, X in sorted(zip(importances, features_list[1:]), reverse=True)]
    print sorted(importances, reverse=True)
