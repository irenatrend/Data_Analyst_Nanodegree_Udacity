import pandas

def add_full_name(path_to_csv, path_to_new_csv):
    #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe, adds a new column
    #called 'nameFull' with a players full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron', 
    #
    #2) Write the data in the pandas dataFrame to a new csv file located at
    #path_to_new_csv

    #WRITE YOUR CODE HERE

    df = pandas.read_csv(path_to_csv)
    df['nameFull'] = df['nameFirst'] + " " + df['nameLast']

    return df.to_csv(path_to_new_csv)

if __name__ == "__main__":
    input_filename =  "Master.csv"
    output_filename = "output.csv"
    add_full_name(input_filename, output_filename)