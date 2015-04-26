import pandas as pd
import ggplot as gg
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''

    #Ridership by day of week - Option 1 (Entries by Day of Week)
    #pd.options.mode.chained_assignment = None  # default='warn'
    #turnstile_weather['weekday'] = pd.to_datetime(turnstile_weather['DATEn']).apply(pd.datetime.weekday)

    #plot = gg.ggplot(turnstile_weather, aes('weekday','ENTRIESn_hourly')) + ggtitle('Entries by Day of Week') + xlab('Day of Week') + ylab('Number  of Entries') +gg.geom_histogram(stat = "bar", position = "stack")+ scale_x_discrete(limits=(-1, 7), breaks=range(0, 7, 1), labels=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    #Ridership by day of week - Option 2 (Avg number of Entries by Day of Week)
    pd.options.mode.chained_assignment = None  # default='warn'
    turnstile_weather['weekday'] = pd.to_datetime(turnstile_weather['DATEn']).apply(pd.datetime.weekday)
    averageentries_on_weekday = turnstile_weather.groupby('weekday', as_index=False).ENTRIESn_hourly.mean()
    averageentries_on_weekday.rename(columns={'ENTRIESn_hourly': 'avg_ENTRIESn_hourly'}, inplace=True)

    plot = gg.ggplot(averageentries_on_weekday, aes('weekday', 'avg_ENTRIESn_hourly')) + ggtitle('Avg number of Entries by Day of Week') + xlab('Day of Week') + ylab('avg number of Entries')  + gg.geom_histogram(stat = "bar", position = "stack") + scale_x_discrete(limits=(-1, 7), breaks=range(0, 7, 1), labels=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

    #Ridership by Unit(Station) - Option 3 (Entries by UNIT)
    #pd.options.mode.chained_assignment = None  # default='warn'

    #plot = gg.ggplot(turnstile_weather, aes('UNIT','ENTRIESn_hourly')) + ggtitle('Entries by UNIT') + xlab('UNIT') + ylab('Number  of Entries') +gg.geom_histogram(stat = "bar", position = "stack") + scale_x_discrete(limits=(-1, 100), breaks=range(0, 100, 1))

    #Ridership by day of week - Option 4 (Avg number of Entries by UNIT)
    #pd.options.mode.chained_assignment = None  # default='warn'

    #averageentries_unit = turnstile_weather.groupby('UNIT', as_index=False).ENTRIESn_hourly.mean()
    #averageentries_unit.rename(columns={'ENTRIESn_hourly': 'avg_ENTRIESn_hourly'}, inplace=True)

    #plot = gg.ggplot(averageentries_unit, aes('UNIT','avg_ENTRIESn_hourly')) + ggtitle('Avg number of Entries by UNIT') + xlab('UNIT') + ylab('avg number of Entries')  + gg.geom_histogram(stat = "bar", position = "stack") + scale_x_discrete(limits=(-1, 50), breaks=range(0, 50, 1))

    return plot


if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb") as f:
        #input_filename = "turnstile_data_master_with_weather.csv"
        turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg = plot_weather_data(turnstile_weather)
        ggsave(image, gg, width=11, height=8)
