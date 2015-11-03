'''
Created on Nov 2, 2015

@author: ams889
'''
import numpy as np

class gridSpace(object):
    #builds the grid to be used for question 4
    def __init__(self, xSamples=500, ySamples=500, xMin=-2, xMax=1, yMin=-1.5, yMax=1.5):
        xSpace = np.linspace(xMin,xMax,xSamples)
        ySpace = np.linspace(yMin,yMax,ySamples)
        xGrid, yGrid = np.meshgrid(xSpace,ySpace)
        self.grid = xGrid + 1j * yGrid
    
    def iteration(self, nMax):    
    # Do the iteration
        np.seterr(all='ignore')
        c = self.grid
        z=c
        for v in range(nMax):
            z = z**2 + c
        return z