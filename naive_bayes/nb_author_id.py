#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")

from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels

features_train, features_test, labels_train, labels_test = preprocess()

# Naive Bayes Training

clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
t1 = time()

print "Training time : ", round(t1-t0, 3), "s"

t2 = time()
pred = clf.predict(features_test)
t3 = time()

print "Prediction time : ", round(t3-t2, 3), "s"

accuracy = accuracy_score(labels_test, pred)

print(accuracy)

#########################################################
### your code goes here ###


#########################################################
