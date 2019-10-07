# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:33:41 2019

@author: nimitha jammula 
"""

import main

class Accuracy:
	def __init__(self, filename):
		csvParser = main.csvParser(self,filename)
		self.Class = csvParser.Class
		self.data = csvParser.data

	def calculateAccuracy(self, root):

		if root == None or len(self.data) == 0:
			self.accuracy = 0
			return 0
		count = 0
		for i in range(0,len(self.data)):
			if self.prediction(root, self.data[i]) == self.Class[i]:
				count += 1

		self.accuracy = 1.0 * count / len(self.data)
        # print self.accuracy
		return self.accuracy

	def prediction(self, root, row):
        # print root.val
        # print row[root.val]
		if root!=None:
			if root.val == -1:
				return root.label
			if row[root.val] == 0:
				return self.prediction(root.left, row)
			else:
				return self.prediction(root.right, row)

	def displayAccuracy(self):
		print('Accuracy on test data :')

		print(str((self.accuracy) * 100) + '%')
