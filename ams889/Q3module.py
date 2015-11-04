'''
Created on Nov 1, 2015

@author: ams889
'''
import numpy as np

def q3output():
    randomArray=np.random.rand(10,3) #generate random array
    arrayLessPt5=np.subtract(randomArray,.5)
    absValArrayLessPt5=np.abs(arrayLessPt5) #take the absolute value of the difference between each element and .5 to establish the correct scale to use
    indicesArgsort=np.argsort(absValArrayLessPt5) #assign indices on every row with relation to closeness to 0
    bestIndex=indicesArgsort[:,0] #create the index vector which stores the result from our argsort index matrix
    indexIncrement=np.arange(0,10) #build a basic incrementing index to use for row indexing
    outputArray=randomArray[[indexIncrement,bestIndex]]
    print outputArray