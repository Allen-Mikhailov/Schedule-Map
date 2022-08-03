from genericpath import exists
from os import remove
import pandas as pd
import numpy as np
import json

# Paths
scheduleDataPath = "./schedules.json"
csvFilePath = "./data.csv"

# Getting schedule data
f = open(scheduleDataPath)
schedules = json.load(f)
f.close()

# Creating index list
index = []
for i in range(7):
    index.append("Period: "+str(i+1))

# Creating new data
teachers = {}
for name in schedules:
    for i in range(len(schedules[name])):
        teacher = schedules[name][i][0]
        period = schedules[name][i][1] - 1

        if (not teachers.__contains__(teacher)):
            teachers[teacher] = np.full((7), "").tolist()
        teachers[teacher][period] += name + ", "
        
        

# Creating dataframe to easily write to file
df = pd.DataFrame(teachers, index=index)

# Writing data
if exists(csvFilePath):
    remove(csvFilePath)
df.to_csv(csvFilePath)