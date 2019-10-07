# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:17:38 2019

@author: nimitha jammula
"""

class Tree_Node:
    """The TreeNode class implements the tree node data structure in the decision tree.
	Attributes:
	    val   : The index of the attribute in current node. A leaf node has a value of -1.
	    label : The most common value in the targetAttribute {0, 1}. A leaf Node is labeled as -1.
	    left  : Root of the left subtree.
	    right : Root of the right subtree.
	"""
    def __init__(self,val, left=None, right=None):
      self.val = val
      self.label = -1
      self.left = left
      self.right = right