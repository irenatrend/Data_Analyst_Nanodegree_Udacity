import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file via the following link:
    https://www.dropbox.com/s/xcn0u2uxm8c4n6l/baseball_data.csv
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """

    #read the csv file into a pandas data frame
    df = pandas.read_csv(filename)

    #create two arrays for left and rigth handed
    lefthanded = df[df['handedness'] == 'L']
    righthanded = df[df['handedness'] == 'R']

    #run t-test
    t_result = scipy.stats.ttest_ind(lefthanded['avg'], righthanded['avg'], equal_var = False)

    if t_result[1] > 0.5:
        return True, t_result
    else:
        return False, t_result


if __name__ == '__main__':
    filename = "baseball_data.csv"
    result = compare_averages(filename)
    print result


#references
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html
