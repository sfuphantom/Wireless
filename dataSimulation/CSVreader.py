from importlib.resources import path
import pathlib
import csv
import json
import pandas as pd
import time
import os

endl = os.linesep

#interval of which to send the corrosponding data in # of data points
dataInterval = .05

#frequency of given data in Hz(for testing purposes; this will be dynamic later on)
dataFrequency = 63
#fileName = "testIMUdata.csv"

#all csvs to have test data created should be in this folder.
simulationPath = "Wireless\\dataSimulation\\Data\\codeTesting"


#will take in a dataPoint, and convert to a json
def data_get(fileLocation):
    #dataFilepath = str(pathlib.Path().resolve()) + "\\Wireless\\dataSimulation\\Data\\" + fileName
    dataFile = open(fileLocation, newline= '')
    sensorData = pd.read_csv(dataFile)
    return sensorData
"""
print(type(sensorData))
print(sensorData)
print(sensorData.index)
print("\n")
print(sensorData.iloc[0][0])
print(sensorData.columns[0])
"""
def data_print(sensorData, t_0, t_1):
    #initial data point time
    t0 = sensorData.iloc[0][0]

    #print (sensorData.iterrows())
    #+1 is to offset that data begins on the second row
    for i in range(t_0+1,t_1+1,1):
        dataPointDICT = {}
        for j in range(0, len(sensorData.columns), 1):
            dataPointDICT[sensorData.columns[j]] = sensorData.iloc[i][j]
    # dataPointJSON(this will need to be sent over mqtt later) = 
        print(json.dumps(dataPointDICT))


#data_print()

#print(os.listdir(str(pathlib.Path().resolve()) + "/Wireless/dataSimulation/Data"))
#print os.listdir(path)
 
#print(os.listdir(str(pathlib.Path().resolve()) + "\Wireless\dataSimulation\Data"))

#print(os.listdir(simulationPath))
    #dataPath = os.path.join(simulationPath, FileName)

#(initial data point, final data point, interval in between)
dataPointSetCount = 2
for i in range (0,9,dataPointSetCount):
    for dataFileName in os.listdir(simulationPath):
        #print(os.path.join(simulationPath, dataFileName))

        #initial and final points in terms of data points
        t_0 = i
        t_1 = i+dataPointSetCount
        if dataFileName.endswith("Full.csv"):
            sensorData = data_get(os.path.join(simulationPath, dataFileName))
            print(endl + "Current data file: " + dataFileName)
            data_print(sensorData, t_0, t_1)
            #print(type(sensorData))
    time.sleep(1.5)

    
#for j in range(0,4,1):
    #print(j)

#str(pathlib.Path().resolve()) + simulationPath + "\\codeTesting" 




"""
    print(dataPointDICT)
    print(type(dataPointDICT))

    print(sensorData.index)

    dataPointJSON = json.dumps(dataPoint)

    print(dataPointJSON)
    print(type(dataPointJSON))

    df = pd.read_csv(dataFile)

    print(df.to_string())

    #initial time the data begins
    #t0

    dataPoint = {
        
    }
"""