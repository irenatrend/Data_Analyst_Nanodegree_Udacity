#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../../final_project/final_project_dataset.pkl", "r"))


print "Number of records:", len(enron_data)  # of records - size of the Enron Dataset
print "Number of features:", len(enron_data['METTS MARK'])  # number of features in the Enron Dataset

# How many POIs are there in the E+F dataset?
numberOfPOIs = 0
for key, value in enron_data.iteritems():
    if enron_data[key]['poi']:
        numberOfPOIs += 1

print "Number of POIs:", numberOfPOIs

# What is the total value of the stock belonging to James Prentice?
print "Total value of the stock belonging to James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]

# How many email messages do we have from Wesley Colwell to persons of interest?
print "Number of messages from Wesley Colwell to POIs:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# What is the value of stock options exercised by Jeffrey Skilling?
print "The value of stock options exercised by Jeffrey Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Of these three individuals (Lay, Skilling and Fastow), who took home the most money
# (largest value of 'total_payments' feature)?
# Jeffrey Skilling, Kenneth Lay, Andrew Fastow
# How much money did that person get?
print "Jeffrey Skilling total payments:", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Kenneth Lay total payments:", enron_data["LAY KENNETH L"]["total_payments"]
print "Andrew Fastow total payments:", enron_data["FASTOW ANDREW S"]["total_payments"]

# How many folks in this dataset have a quantified salary? What about a known email address?

peopleWithQuantifiedSalary = 0
peopleWithQuantifiedEmailAddress = 0
nanTotalPayments = 0
nanTotalPaymentsPOI = 0

for key, value in enron_data.iteritems():
    print enron_data[key]["salary"]

    if enron_data[key]['salary'] != 'NaN':
        peopleWithQuantifiedSalary += 1
    if enron_data[key]['email_address'] != 'NaN':
        peopleWithQuantifiedEmailAddress += 1
    if enron_data[key]['total_payments'] == 'NaN':
        nanTotalPayments += 1
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi']:
        nanTotalPaymentsPOI += 1



print "Number of people with Quantified Salary:", peopleWithQuantifiedSalary
print "Number of people with Quantified Email Address:", peopleWithQuantifiedEmailAddress
print "Number of people with NaN Total Payments:", nanTotalPayments

# How many people in the E+F dataset (as it currently exists) have 'NaN'
# for their total payments? What percentage of people in the dataset as a whole is this?
print "% of the people in the dataset that don't have total_payments filled in:", (nanTotalPayments / float(len(enron_data))) * 100

# How many POIs in the E+F dataset have 'NaN' for their total payments?
# What percentage of POI's as a whole is this?
print "% of the POIs in the dataset that don't have total_payments filled in:", (nanTotalPaymentsPOI / float(len(enron_data))) * 100


# references
# https://docs.python.org/2/library/pickle.html