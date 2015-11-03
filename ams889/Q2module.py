'''
Created on Nov 1, 2015

@author: ams889
'''
import numpy as np

def q2output():
    a = np.arange(25).reshape(5, 5) #given array
    b = np.array([1., 5, 10, 15, 20]) #divide columns of array 'a' by b
    arrayDivided = np.divide(a.transpose(),b).transpose() #transposes a and uses row-based element wise dividion function; returns transpose of result to original array format
    print "Q2 Result: \n", arrayDivided