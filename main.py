# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:01:03 2019

@author: nimitha jammula
"""

import ID3
import sys
import Accuracy
import csv
import pandas as pd

def main():

    train_file=str(sys.argv[1]) ;
    attribute_names_adder(train_file)
    validation_file = sys.argv[2]
    attribute_names_adder(validation_file)
    test_file= sys.argv[3]
    attribute_names_adder(test_file)
    yesno = str(sys.argv[4])
    heu = str(sys.argv[5])
    pru = str(sys.argv[6])
    L = int(sys.argv[7])
    K = int(sys.argv[8])
    decisionTree = ID3.DTree(train_file,heu)
    if yesno == "yes":
        print('Decision Tree before Pruning:')
        print(decisionTree)

    accuracy = Accuracy.Accuracy(test_file)
    accuracy.calculateAccuracy(decisionTree.root)
    print('Accuracy before Pruning:')
    accuracy.displayAccuracy()
    
    if(pru == 'r'):  
        decisionTree.pruneTree(L,K,validation_file)
    elif(pru == 'n'):
        print('No pruning')
        return
    if yesno == "yes":
        print('Decision Tree after Pruning :')
        print(decisionTree)
    accuracy.calculateAccuracy(decisionTree.root)
    print('Accuracy after Pruning:')
    accuracy.displayAccuracy()

def csvParser(self, filename):
    self.data = []
    with open(filename,'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        count = 0
        for row in csvreader:
            if count == 0:
                self.attributeNames = row[:-1]
            else:
                self.data.append([int(i) for i in row])
            count += 1

    self.attributes = range(len(self.attributeNames))
    self.trainingValues = range(len(self.data))
    self.Class = [row[-1] for row in self.data]
    return self



def attribute_names_adder(filePath):
   data = pd.read_csv(filePath,sep = ',',header = 0)
   #print('Data Set length :',len(data))
   #print('Data Set shape :',data.shape)
   for i, (ca,cc) in zip(range(len(data.columns)), data.iteritems()): 
      name = 'X'+str(i)
      data.rename(columns={ca : name}, inplace=True)
   data.rename(columns={ data.columns[len(data.columns)-1]: "Class" }, inplace = True)
   data.to_csv(filePath, index=False)

if __name__ == '__main__':
    main()