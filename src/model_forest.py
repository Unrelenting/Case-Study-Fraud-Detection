from __future__ import division
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from collections import Counter
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import f1_score, make_scorer
from sklearn.ensemble import RandomForestClassifier
from utils import *
import random
import cPickle as pickle

if __name__ == "__main__":
    # Load data
    df = pd.read_json('../data.json')

    # Preprocess data
    X, y = preprocess(df)

    # train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)

    # Builds cost matrix
    cost_matrix = make_scorer(build_cost_matrix)

    # Our first model: Logistic Regression
    # lr = LogisticRegression()
    # model = lr.fit(X_train, y_train)
    #
    # print "accuracy is {}".format(model.score(X_test, y_test))
    # print "f1 score is {}".format(f1_score(model.predict(X_test), y_test))
    # print "cross val f1 score is {}".format((np.mean(cross_val_score(lr, X_train, y_train, scoring='f1'))))
    # print "cross val cost score is {}".format((np.mean(cross_val_score(lr, X_train, y_train, scoring=cost_matrix))))

    print "\n\n\n"

    # Our second model: Random Forest
    rf = RandomForestClassifier(max_depth=5, n_estimators=10)
    rf_model = rf.fit(X_train, y_train)

    print "accuracy is {}".format(rf_model.score(X_test, y_test))
    print "f1 score is {}".format(f1_score(rf_model.predict(X_test), y_test))
    print "cross val f1 score is {}".format((np.mean(cross_val_score(rf, X_train, y_train, scoring='f1'))))
    print "cross val cost score is {}".format((np.mean(cross_val_score(rf, X_train, y_train, scoring=cost_matrix))))
