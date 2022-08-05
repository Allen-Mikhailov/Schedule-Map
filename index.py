from genericpath import exists
from os import remove
import pandas as pd
import numpy as np
import json

# Paths
scheduleDataPath = "./schedules.json"
csvFilePath = "./data.csv"

# Checking for data
if not exists(scheduleDataPath):
    print("Path \""+scheduleDataPath+"\" does not exist")
    quit()

# Getting schedule data
f = open(scheduleDataPath)
data = json.load(f)
schedules = data["students"]
teacherData = data["teachers"]
f.close()

# Creating index list
index = []
for i in range(7):
    index.append("Period: "+str(i+1))
index.append("A Lunch")
index.append("B Lunch")
index.append("C Lunch")

lunches = {
    "A": "",
    "B": "",
    "C": ""
}

firstTeacher = ""

# Creating new data
dataFrame = {}
for name in schedules:
    for i in range(len(schedules[name])):
        teacher = schedules[name][i]
        period = i

        # First Teacher
        if firstTeacher == "":
            firstTeacher = teacher

        # Lunch
        if period == 4:
            if teacherData.__contains__(teacher):
                lunch = teacherData[teacher]["Lunch"]
                lunches[lunch] += name +", "
            else:
                print("Warning: No teacher data for \"" + teacher +"\"")


        if (not dataFrame.__contains__(teacher)):
            dataFrame[teacher] = np.full((10), "").tolist()
        dataFrame[teacher][period] += name + ", "

# Adding Lunches to dataFrame
dataFrame[firstTeacher][7] = lunches["A"]
dataFrame[firstTeacher][8] = lunches["B"]
dataFrame[firstTeacher][9] = lunches["C"]

# Creating dataframe to easily write to file
df = pd.DataFrame(dataFrame, index=index)

# Writing data
if exists(csvFilePath):
    remove(csvFilePath)
df.to_csv(csvFilePath)