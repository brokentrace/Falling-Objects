# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:07:03 2016

@author: erik
"""

import fallingObjects as fo
import pandas as pd
import time

seconds = 5
timeDelta = .001
currentTime = 0

objectData = pd.DataFrame()

startTime = time.time()

print ("Calculation Started")

while currentTime <= seconds: #Generate a time step series of calculations
    data = pd.DataFrame({'Velocity': round(fo.velocity(currentTime),4), 'Distance': round(fo.distance(currentTime),4)},index=[currentTime])
    currentTime = currentTime + timeDelta
    objectData = objectData.append(data)
   # percentComplete = round((currentTime/seconds)*100,4)
   # print ("Percent Complete: " + str(percentComplete) + "%")
    
LoopEndTime = time.time()
print('Number of calculations: ' + str(len(objectData)))

plotStart = time.time()
objectData.plot()
plotEnd = time.time()

totalLoopTime = round((LoopEndTime - startTime),4)
totalPlotTime = round((plotEnd - plotStart),4)

print('Times are:')
print('Loop Time: ' + str(totalLoopTime))
print('Plot Time: ' + str(totalPlotTime))