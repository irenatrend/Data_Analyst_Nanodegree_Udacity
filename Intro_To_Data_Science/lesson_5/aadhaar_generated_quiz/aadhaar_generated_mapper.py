import sys
import logging
import string

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    logging.info("My debugging message")
        
    for line in sys.stdin:
        #your code here
        #data = line.strip().split(" ")
        #logging.info(len(data))
        
        #for word in data:
        #    logging.info(word)
        #    cleaned_data = word.translate(string.maketrans(" ",""), string.punctuation).lowercase()
        #    print "{0}\t{1}".format(word, 1)
        ####
        data = line.strip().split(",")

        #skip header
        if data[0] == 'Registrar':
            logging.info("Header skipped: %s", data)
            continue

        #skip rows without the correct number of tokens
        if len(data) != 12:
            logging.info("rows without the correct number of tokens skipped: %s", data)
            continue

        print "{0}\t{1}".format(data[3], data[8])

mapper()
