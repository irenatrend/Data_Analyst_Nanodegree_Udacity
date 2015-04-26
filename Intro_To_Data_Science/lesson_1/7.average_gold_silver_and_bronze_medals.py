import numpy
from pandas import DataFrame, Series


def avg_medal_count():
    '''
    Using the dataframe's apply method, create a new Series called 
    avg_medal_count that indicates the average number of gold, silver,
    and bronze medals earned amongst countries who earned at 
    least one medal at the 2014 Sochi olympics.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    
    # your code here
    olympic_medal_counts = {'country_name': Series(countries),
     'gold': Series(gold),
     'silver': Series(silver),
     'bronze': Series(bronze)}

    olympic_medal_counts_df = DataFrame(olympic_medal_counts)
    #at_least_one_medal = olympic_medal_counts_df[(olympic_medal_counts_df['gold'] <> 0) & (olympic_medal_counts_df['silver'] <> 0) & (olympic_medal_counts_df['bronze'] <> 0)]
    
    olympic_medal_counts_df = olympic_medal_counts_df[['gold', 'silver', 'bronze']]
   
    avg_medal_count = olympic_medal_counts_df.apply(numpy.mean)
      
    return avg_medal_count

if __name__ == '__main__':
    print avg_medal_count()