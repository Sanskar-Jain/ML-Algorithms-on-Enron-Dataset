#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    data = []
    for i in range(len(predictions)):
        data.append((predictions[i][0],ages[i][0],net_worths[i][0],net_worths[i][0]-predictions[i][0]))
    data = sorted(data, key=lambda d: abs(d[2]-d[0]))
    cleaned_data = []
    for i in range(len(data)*90/100):
        cleaned_data.append((data[i][1],data[i][2],data[i][3]))
    return cleaned_data

