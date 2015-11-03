'''
Created on Nov 1, 2015

@author: ams889
'''
import numpy as np

def q1output():
    first2Darray = np.arange(1, 16) #generates array values
    arrayReshape = first2Darray.reshape(3,5) #reshapes values into array format
    arrayTransposed = arrayReshape.transpose() #transposes array to desired format
    print "Q1 Initial Array: \n", arrayTransposed
    row2and4=arrayTransposed[1:4:2] #return 2nd and 4th rows
    print "Q1A: \n",  row2and4
    column2=arrayTransposed[:,1] #return 2nd column
    column2AsColumn=column2.reshape(5,1)
    print "Q1B: \n",  column2AsColumn
    rows2to4=arrayTransposed[1:4:2] #return 2nd to 4th column AKA rectangular section between [1,0] and [3,2]
    print "Q1C: \n",  rows2to4
    valsover3=arrayTransposed[arrayTransposed>3] #return values in array above 3
    valsover3under11=valsover3[valsover3<11] #return values in array already limited to be greater than 3, below 11
    print "Q1D: \n",  valsover3under11