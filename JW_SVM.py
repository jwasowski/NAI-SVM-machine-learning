# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:43:51 2019

@author: Kuba
"""

import numpy as np
import math, sys
import argparse
from sklearn import linear_model
import sklearn.metrics as sm
import pickle

#{"class value" as int : ["cash range start value" as int,"cash range length value" as int]}
classification_model = {1:[20, 5], 2:[25,2], 3:[27,3], 4:[30,3], 5:[33,3], 6:[36,3], 7:[39,3],
                        8:[42,3], 9:[45,3], 10:[48,4], 11:[52,4], 12:[56,4], 13:[60,5], 14:[65,5],
                        15:[70,5], 16:[75,5], 17:[80,10]}

#Calculates predicted values based on classification_model
#Returned value equation: cash range start value + cash range length value * predicted_class fractional part
def calculate_predicted_value(predicted_class):
    predicted_class_array = math.modf(predicted_class)
    predicted_value = classification_model[predicted_class_array[1]][0]+ \
    classification_model[predicted_class_array[1]][1]*predicted_class_array[0]
    
    return predicted_value

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Calculates predicted value of 100km ride')
    parser.add_argument('-l', nargs='+',  dest='params', required=True,
            help='Input user')
    return parser

def main():
    args = build_arg_parser().parse_args()
    args_data = args.params
    args_data = args_data[0].split(',')
    try:
        test_data = [float(args_data[0]), int(args_data[1]), float(args_data[2]), int(args_data[3])]
    except:
        sys.exit("ERROR: Wrong arguments \n Example arguments: 1.6,125,7.8,1")
        
    try:
        with open("learned_model.pkl", 'rb') as f:
            regressor = pickle.load(f)
        
    except IOError:
        print("File is not there, generate it first!")
        print("Learning and generating file!")
        data_inputfile = "learning_data_set.txt"
        class_data = "data_classification.txt"
        data = np.loadtxt(data_inputfile, delimiter=',')
        data_class = np.loadtxt(class_data)
        
        X, y = data[:], data_class[:]
        
        num_training = int(len(X)*0.9)
        
        X_tran, y_train = X[:num_training], y[:num_training]
        X_test, y_test = X[num_training:], y[num_training:]

        print("\n")
        print(X_test)
        print(y_test)
        
        regressor = linear_model.HuberRegressor()
        regressor.fit(X_tran, y_train)
        y_test_pred = regressor.predict(X_test)
        print("\nTest predictions")
        print(y_test_pred)
        
        blad = sm.mean_absolute_error(y_test, y_test_pred)
        print ("\nMean absolute error: ", blad)
        
        with open("learned_model.pkl", 'wb') as f:
            pickle.dump(regressor, f)
            print("Writting model into file!")
    
    
    finally:

        #test_data = [1.6,165,7.7,1]
        predicted_class = regressor.predict([test_data])
        print("\nPredicted cost category per 100km ride:", calculate_predicted_value(predicted_class))

if __name__ == '__main__':
    main()