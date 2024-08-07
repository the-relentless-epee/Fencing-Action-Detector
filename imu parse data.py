import csv
import numpy as np

DATA_LEN = 16

def dataToArray(path):
    with open(path, "r") as file:
        RawString = file.readlines()
        RowNum = len(RawString)
        timeStamp = np.zeros((RowNum, 1), dtype=object) #initialize timestamp data array
        dataArray = np.zeros((RowNum, DATA_LEN), dtype=object) #initialize data array
        for i in range(RowNum):
            splitString = RawString[i].split(",")
            timeStamp[i, 0]=splitString[0]
            acceleration = splitString[2:5:1]
            angularVelocity = splitString[6:9:1]
            angle = splitString[10:13:1]
            MagneticDir = splitString[14:17:1]
            quaternion = splitString[18:22:1]
            arrayOfArrays = (acceleration, angularVelocity, angle, MagneticDir, quaternion)
            dataArray[i, 0:(sum(len(x) for x in [acceleration, angularVelocity, angle, MagneticDir, quaternion]))] = np.concatenate(arrayOfArrays)
            dataArray = dataArray.astype(float)
        return dataArray

            

print(dataToArray("data.txt"))
