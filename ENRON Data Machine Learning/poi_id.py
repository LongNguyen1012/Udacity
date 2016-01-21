# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:46:15 2016

@author: Long Nguyen
"""

#!/usr/bin/python

import sys
import pickle
import numpy as np
sys.path.append("../tools/")

from feature_format import featureFormat
from tester import dump_classifier_and_data
from sklearn.preprocessing import MinMaxScaler
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectPercentile

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
          
actual_feature_list = ['poi','dummy']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
outliers = ["TOTAL","THE TRAVEL AGENCY IN THE PARK","LOCKHART EUGENE E"]

for key in outliers:
    data_dict.pop(key, 0)

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

### Task 4: Feature Engineering
index = 0
for person in my_dataset:
    
    total_missing = 0   

    ### These features are excluded because all pois have these features while some non-poi
    ### have these features missing
    exclude_list = ['total_payments','total_stock_value','expenses','other','email_address']

    my_dataset[person]['dummy'] = 1
         
    for feature in my_dataset[person].keys():
        if feature not in exclude_list:
            missing_feature_name = "missing_" + feature
            my_dataset[person][missing_feature_name] = 0
            if my_dataset[person][feature] == "NaN":
                my_dataset[person][feature] = 0
                my_dataset[person][missing_feature_name] = 1
                total_missing += 1
            else:
                my_dataset[person][missing_feature_name] = 0
    my_dataset[person]['total_missing'] = total_missing
    
    my_dataset[person]['originally_missing'] = total_missing

    
    my_dataset[person]['no_missing_vs_no_original_features'] = float(total_missing)/15


    my_dataset[person]['deferred_income'] = abs(my_dataset[person]['deferred_income'])


    if my_dataset[person]['salary'] != 0:    
        my_dataset[person]['bonus_vs_salary'] = float(my_dataset[person]['bonus'])/my_dataset[person]['salary']
        my_dataset[person]['missing_bonus_vs_salary'] = 0
    else:
        my_dataset[person]['bonus_vs_salary'] = 0
        my_dataset[person]['missing_bonus_vs_salary'] = 1
        my_dataset[person]['total_missing'] += 1
        
        
    if (my_dataset[person]['to_messages'] + my_dataset[person]['from_messages']) != 0:
        my_dataset[person]['poi_interaction'] = float((my_dataset[person]['from_poi_to_this_person'] + \
                                               my_dataset[person]['from_this_person_to_poi'])) / \
                                               (my_dataset[person]['from_messages'] + \
                                               my_dataset[person]['to_messages'])
        my_dataset[person]['missing_poi_interaction'] = 0
    else:
        my_dataset[person]['poi_interaction'] = 0
        my_dataset[person]['missing_poi_interaction'] = 1
        my_dataset[person]['total_missing'] += 1

    
    
    my_dataset[person]['total_long_term_incentive'] = my_dataset[person]['long_term_incentive'] + \
                                                     my_dataset[person]['restricted_stock'] + \
                                                     my_dataset[person]['deferred_income']
    
    
    my_dataset[person]['total_current_compensation'] = my_dataset[person]['salary'] + \
                                                      my_dataset[person]['bonus'] + \
                                                      my_dataset[person]['deferral_payments'] + \
                                                      my_dataset[person]['director_fees'] + \
                                                      my_dataset[person]['exercised_stock_options'] + \
                                                      my_dataset[person]['restricted_stock'] - \
                                                      my_dataset[person]['restricted_stock_deferred']
        
                                                 
    if my_dataset[person]['total_current_compensation'] != 0:
        my_dataset[person]['money_left_on_table'] =  float(my_dataset[person]['total_long_term_incentive']) / \
                                                    my_dataset[person]['total_current_compensation']
        my_dataset[person]['missing_money_left_on_table'] = 0                                                    
    else:
        my_dataset[person]['money_left_on_table'] = 0
        my_dataset[person]['missing_money_left_on_table'] = 1
        my_dataset[person]['total_missing'] += 1
        
        
    my_dataset[person]['from_poi_larger_than_to_poi'] = 0
    my_dataset[person]['from_poi_smaller_than_to_poi'] = 0
    my_dataset[person]['from_poi_equal_to_poi'] = 0    
    if my_dataset[person]['from_poi_to_this_person'] > my_dataset[person]['from_this_person_to_poi']:
        my_dataset[person]['from_poi_larger_than_to_poi'] = 1
    if my_dataset[person]['from_poi_to_this_person'] < my_dataset[person]['from_this_person_to_poi']:
        my_dataset[person]['from_poi_smaller_than_to_poi'] = 1
    if my_dataset[person]['from_poi_to_this_person'] == my_dataset[person]['from_this_person_to_poi']:
        my_dataset[person]['from_poi_equal_to_poi'] = 1
        
        
    my_dataset[person]['restricted_stock_larger_than_restricted_stock_deferred'] = 0
    my_dataset[person]['restricted_stock_equal_restricted_stock_deferred'] = 0   
    if my_dataset[person]['restricted_stock'] > my_dataset[person]['restricted_stock_deferred']:
        my_dataset[person]['restricted_stock_larger_than_restricted_stock_deferred'] = 1
    if my_dataset[person]['restricted_stock'] == my_dataset[person]['restricted_stock_deferred']:
        my_dataset[person]['restricted_stock_equal_restricted_stock_deferred'] = 1
        
    
    my_dataset[person]['total_missing_vs_all_features'] = float(my_dataset[person]['total_missing'])/54 
    
    index += 1
    my_dataset[person]['index'] = index
    
### List of numeric features needed to be scaled
new_features_list = ['dummy','bonus_vs_salary','director_fees','from_messages','from_poi_to_this_person', \
                     'total_long_term_incentive','bonus','deferral_payments','deferred_income', \
                     'exercised_stock_options','long_term_incentive', \
                     'restricted_stock','restricted_stock_deferred','salary', \
                     'total_current_compensation','originally_missing','total_missing', \
                     'from_this_person_to_poi','loan_advances', \
                     'money_left_on_table','shared_receipt_with_poi','to_messages']

temp_feature_list = []

### Find the name of the remaining features 
exclude_list = ['total_payments','total_stock_value','expenses','other', \
                'email_address','poi','missing_dummy','missing_poi','index']
  
for key in my_dataset['ALLEN PHILLIP K'].keys():
    if (key not in new_features_list) & (key not in exclude_list):
        temp_feature_list.append(key)

temp_feature_list.append('index')

### Scale the data                    
data = featureFormat(my_dataset, new_features_list )
data = np.delete(data,0,1)
scaler = MinMaxScaler()
data = scaler.fit_transform(data)

### Complete data after scaling
temp_data = featureFormat(my_dataset, temp_feature_list)
features = np.hstack((data, temp_data))

### Extract final features list
features_list = []
for feature in new_features_list:
    features_list.append(feature)
    
for feature in temp_feature_list:
    features_list.append(feature)
    
features_list.pop(0)

### Turn features back in to dictionary data set
for person in my_dataset:
    for row in range(len(features)):
        if my_dataset[person]['index'] == features[row][47]:
            for feature in features_list:
                idx = features_list.index(feature)
                my_dataset[person][feature] = features[row][idx]
                
features_list.pop()
features_list.insert(0,'poi')

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html
from sklearn.ensemble import AdaBoostClassifier

pipeline = make_pipeline(PCA(), SelectPercentile(), AdaBoostClassifier())

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
param_grid = dict(pca__n_components = [14,16,18,20], \
                  selectpercentile__percentile = [25,50,75,100], \
                  adaboostclassifier__n_estimators = [20,40,60])
 
from sklearn.metrics import fbeta_score, make_scorer    
            
scorer = make_scorer(fbeta_score, beta = 1e100)
clf = GridSearchCV(pipeline, param_grid, scoring = scorer)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)