from genericpath import exists
from os import remove
import pandas as pd
import openpyxl
import numpy as np
import json

# Paths
scheduleDataPath = "./schedules.json"
outputPath = "./data.xlsx"

def correctName(str):
    return str[:1].upper() + str[1:].lower()

def rectObj(obj):
    longest = 0
    for key in obj:
        if len(obj[key]) > longest:
            longest = len(obj[key])
    for key in obj:
        while (len(obj[key]) < longest):
            obj[key].append("")
    

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
periodIndex = []
for i in range(7):
    periodIndex.append("Period: "+str(i+1))

lunchNames = {"A": "A Lunch", "B":"B Lunch", "C":"C Lunch"}

lunchObj = {
    "A": [],
    "B": [],
    "C": []
}

# Creating new data
teacherObj = {}
for name in schedules:
    schedule = schedules[name].split(",")
    for i in range(len(schedule)):
        teacher = correctName(schedule[i])
        period = i

        # Lunch
        if period == 4:
            if teacherData.__contains__(teacher):
                lunch = teacherData[teacher]["Lunch"]
                lunchObj[lunch].append(name)
            else:
                print("Warning: No teacher data for \"" + teacher +"\"")


        if (not teacherObj.__contains__(teacher)):
            teacherObj[teacher] = np.full((7), "").tolist()
        # print(period)
        teacherObj[teacher][period] += name + ", "

studentMatches = {}
for name in schedules:
    studentMatches[name] = np.full((7), "")
    

rectObj(lunchObj)

# Creating dataframe to easily write to file
teacherDF = pd.DataFrame(teacherObj, index=periodIndex)
lunchesDF = pd.DataFrame(lunchObj)

# Writing data
if exists(outputPath):
    remove(outputPath)

writer = pd.ExcelWriter(outputPath)

teacherDF.to_excel(writer, sheet_name="Teachers")
lunchesDF.to_excel(writer, sheet_name="Lunches")

writer.close()