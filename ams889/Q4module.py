'''
Created on Nov 1, 2015

@author: ams889
'''
import numpy as np
import matplotlib.pyplot as plt
from gridClass import gridSpace

def q4output(nMax, threshold):
    #run the gridSpace class for our chosen inputs
    fractal=gridSpace() #uses default parameters of xSamples=ySamples=500, xMin=-2, xMax=1, yMin=-1.5, yMax=1.5
    fractalIteration = fractal.iteration(nMax)
    boolMask = np.abs(fractalIteration) < threshold
    plt.imshow(boolMask, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')
