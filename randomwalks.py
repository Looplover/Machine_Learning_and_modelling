#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:08:41 2023

@author: shrenikmohansakala
"""

import random
import numpy
import pylab
import matplotlib.pyplot as plt

class Field(object):
    def __init__(self):
        self.Drunks = []
        
    def getDrunks(self):
        return self.Drunks
    
    
class Location(object):
    def __init__(self,Xvalue,Yvalue):
        self.X = Xvalue
        self.Y = Yvalue
        
    def distance(self,other):
        return ((self.X - other.X)**2 + (self.Y - other.Y)**2)**(0.5)
    
    def newLocation(self,shift):
        self.X += shift[0]
        self.Y += shift[1]
    
    
    def __str__(self):
        return "(" + str(self.X) + "," + str(self.Y) + ")"
    

class Drunk(object):
    def __init__(self,name,Xvalue,Yvalue):
        self.Name = name
        self.Position = Location(Xvalue,Yvalue)
        
    def getName(self):
        return self.Name
    
    def getPos(self):
        return self.Position
    
    def setPos(self,new):
        self.Position = new
        
    def __str__(self):
        return str(self.Name)
    
    
class normalDrunk(Drunk):
    def __init__(self,name,Xvalue,Yvalue):
            Drunk.__init__(self,name,Xvalue,Yvalue)
            self.Shift = [(1,0),(-1,0),(0,1),(0,-1)]
            
    def getShift(self):
        return self.Shift
        

class weirdDrunk(Drunk):
    def __init__(self,name,Xvalue,Yvalue):
            Drunk.__init__(self,name,Xvalue,Yvalue)
            self.Shift = [(1,0),(-1,0),(0,0.9),(0,-1.1)]
            
    def getShift(self):
        return self.Shift
    
    
    
def oneDrunk(type,numSteps,start):
    drunk = type(1,start.X,start.Y)
    for i in range(numSteps):
        shift = random.choice(drunk.getShift())
        position = drunk.getPos()
        position.newLocation(shift)
        drunk.setPos(position)
        
    return drunk.getPos().distance(start)


def simDrunk(type,numDrunks,numSteps,start):
    drunks = []
    for j in range(numDrunks):
        drunks.append(oneDrunk(type,numSteps,start))
    return (numpy.mean(drunks),numpy.std(drunks))
            
random.seed(0) 
print("Normal")
print(simDrunk(normalDrunk, 100,2, Location(0,0)))
print("Weird")
print(simDrunk(weirdDrunk, 100,2, Location(0,0)))


def distDrunk(type,numSteps,start,precision):
    numDrunks= 100
    mean,std = simDrunk(type,numDrunks,numSteps,start)
    while mean <= 0 and (std  - (precision/2)) > 0 :
        mean,std = simDrunk(type,numDrunks,numSteps,start)
        numDrunks *= 2
        
    return mean

steps = [1,10,100,10000]
distances1 = [distDrunk(normalDrunk, x, Location(0,0), 0.05) for x in steps]
distances2 = [distDrunk(weirdDrunk, x, Location(0,0), 0.05) for x in steps]


#pylab.plot(steps,distances1,'-r')
#pylab.plot(steps,distances2,'-c') 

def scatterDrunk1(type,numDrunks,numSteps,start,color):
        X = []
        Y = []
        for j in range(numDrunks):
            X.append(j)
            Y.append(oneDrunk(type,numSteps,start))
        plt.scatter(X,Y,color=color)
        
#scatterDrunk1(normalDrunk,100,2,Location(0,0),"red")
#scatterDrunk1(weirdDrunk,100,2,Location(0,0),"blue")


def coordDrunk(type,numSteps,start):
    drunk = type(1,start.X,start.Y)
    for i in range(numSteps):
        shift = random.choice(drunk.getShift())
        position = drunk.getPos()
        position.newLocation(shift)
        drunk.setPos(position)
        
    return drunk.getPos()

def scatterDrunk2(type,numDrunks,numSteps,start,color):
        X = []
        Y = []
        for j in range(numDrunks):
            x,y = coordDrunk(type,numSteps,start).X,coordDrunk(type,numSteps,start).Y
            X.append(x)
            Y.append(y)
        plt.scatter(X,Y,color=color)
        
scatterDrunk2(normalDrunk,10000,100,Location(0,0),"red")
scatterDrunk2(weirdDrunk,10000,100,Location(0,0),"blue")
    
            