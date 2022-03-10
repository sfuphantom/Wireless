from importlib.resources import path
import pathlib
import csv
import json
from sqlite3 import DataError
import pandas as pd
import time
import os
import threading

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

#(initial data point, final data point, interval in between)
def main():
    t1 = threading.Thread(target=data_print)
    #pulling in initial data from csv files
    fullData = {}
    sensors = []
    
    for dataFileName in os.listdir(simulationPath):
        if dataFileName.endswith("Full.csv"): #condition on files, but not needed if all files are to be pulled in
            sensorData = data_get(os.path.join(simulationPath, dataFileName))
            fullData [dataFileName] = sensorData
            sensors.append(dataFileName)

    dataPointSetCount = 2
    for i in range (0,3,dataPointSetCount):
        #data_print(fullData)
        for dataFileName in os.listdir(simulationPath):

            #initial and final points in terms of data points
            t_0 = i
            t_1 = i+dataPointSetCount
            for fileName in sensors:
                sensorData = fullData[fileName]
                print(endl + "Current data file: " + fileName)
                data_print(sensorData, t_0, t_1)
            
        time.sleep(1.5)

main()
