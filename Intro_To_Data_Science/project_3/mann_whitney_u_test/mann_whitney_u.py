import numpy as np
import scipy
import scipy.stats
import pandas as pd


def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing our final turnstile-Subway data. This 
    function should return the mean number of entries with rain, the mean number of entries without rain, and the
    Mann-Whitney U statistic and p-value.  You should feel free to use scipy's Mann-Whitney implementation, and also
    might find it useful to use numpy's mean function.  Here's some documentation on that:

    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    '''

    with_rain_mean = np.mean(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==1])
    without_rain_mean = np.mean(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==0])

    U, p = scipy.stats.mannwhitneyu(turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==1], turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain']==0], use_continuity=False)

    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_output = mann_whitney_plus_means(turnstile_master)

    print student_output


#reference
#http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.mannwhitneyu.html