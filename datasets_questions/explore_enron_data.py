#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import cPickle

enron_data = cPickle.load(open("../final_project/final_project_dataset.pkl", 'r'))

print(enron_data)
print len(enron_data)

count = [0,0]
for poi in enron_data:
    if enron_data[poi]['total_payments'] == 'NaN':
        count[0] += 1
    if enron_data[poi]['poi'] == 1:
        count[1] += 1

print(count[0])
print count[0]*100/count[1]
