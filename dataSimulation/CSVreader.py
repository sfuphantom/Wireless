import pathlib
import csv
import json
import pandas as pd

#period in seconds
dataPeriod = 1.0
fileName = "testIMUdata.csv"

#will take in a dataPoint, and convert to a json
dataFilepath = str(pathlib.Path().resolve()) + "\\Wireless\\dataSimulation\\Data\\" + fileName
dataFile = open(dataFilepath, newline= '')
sensorData = pd.read_csv(dataFile)

"""
print(type(sensorData))
print(sensorData)
print(sensorData.index)
print("\n")
print(sensorData.iloc[0][0])
print(sensorData.columns[0])
"""

#initial data point time
t0 = sensorData.iloc[0][0]

#print (sensorData.iterrows())
for i in sensorData.index:
    dataPointDICT = {
        sensorData.columns[0]: sensorData.iloc[i][0],
        sensorData.columns[1]: sensorData.iloc[i][1],
        sensorData.columns[2]: sensorData.iloc[i][2],
        sensorData.columns[3]: sensorData.iloc[i][3],
        sensorData.columns[4]: sensorData.iloc[i][4],
        sensorData.columns[5]: sensorData.iloc[i][5],
        sensorData.columns[6]: sensorData.iloc[i][6],
        sensorData.columns[7]: sensorData.iloc[i][7]
    }
    dataPointJSON = json.dumps(dataPointDICT)
    print(dataPointJSON)

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