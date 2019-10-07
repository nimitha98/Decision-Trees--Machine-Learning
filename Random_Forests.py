# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:07:02 2019

@author: nimitha jammula
"""

  
# Random Forest Classification

# Importing the libraries
import numpy as np
import pandas as pd
import sys

def attribute_names_adder(filePath):
   '''
    This is used to add the attribute labels to the columns in the datasets
   '''
   data = pd.read_csv(filePath,sep = ',',header = 0)
   #print('Data Set length :',len(data))
   print('Data Set shape :',data.shape)
   for i, (ca,cc) in zip(range(len(data.columns)), data.iteritems()): 
      name = 'X'+str(i)
      data.rename(columns={ca : name}, inplace=True)
   data.rename(columns={ data.columns[len(data.columns)-1]: "Class" }, inplace = True)
   data.to_csv(filePath, index=False)

#alternatively you can get the dataset using
#https://archive.ics.uci.edu/ml/machine-learning-databases/housing/
#Taking  the input from the console
train_data_path = str(sys.argv[1])
valid_data_path = str(sys.argv[2])
test_data_path = str(sys.argv[3])


attribute_names_adder(train_data_path)
attribute_names_adder(valid_data_path)
attribute_names_adder(test_data_path)

#reading the csv file with pandas
train_data=pd.read_csv(train_data_path)
valid_data = pd.read_csv(valid_data_path)
test_data = pd.read_csv(test_data_path)

#Summary Statistics
print(train_data.describe())

#split x and y
x_train = train_data.drop('Class', axis = 1)
y_train = train_data['Class']

x_valid = train_data.drop('Class', axis = 1)
y_valid = valid_data['Class']

x_test = train_data.drop('Class', axis = 1)
y_test = train_data['Class']


# Fitting Random Forest Regression to the Training set
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 50, random_state = 0)
regressor.fit(x_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(x_test)


# Evaluating the Algorithm
from sklearn.metrics import mean_absolute_error, mean_squared_error, classification_report, confusion_matrix, accuracy_score
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, y_pred)))

print('The confusion matrix:')
print(confusion_matrix(y_test,y_pred.round()))
print('Classification Report')
print(classification_report(y_test,y_pred.round()))
print('The accuracy with the Random forest: ')
print((accuracy_score(y_test, y_pred.round()))*100)
