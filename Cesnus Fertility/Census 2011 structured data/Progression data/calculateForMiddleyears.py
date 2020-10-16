# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 14:20:31 2020

@author: JAYU
"""
import json
import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict
import csv


def processAreaName(areaName):
    temp = areaName.lower().replace(' ','').replace('district','').replace('state','').replace('-','').replace('*','')
    for i in range(0, 10):
        temp = temp.replace(str(i),'')
    return temp

def processAreaType(areaType):
    temp = areaType.lower().replace(' ','')
    return temp

def processAgeName(ageName):
    temp = ageName.lower().replace(' ','')
    return temp

################## PROGRAM | START ##################

# raw_data1 and raw_data2 csv files for data before 04/25/2020
with open("Gujrat_district-Total Women,married women, children 2011.csv") as csvFile1:
    rawdata2011 = pd.read_csv(csvFile1)
with open("Gujrat_district-Total Women,married women, children 2001.csv") as csvFile2:
    rawdata2001 = pd.read_csv(csvFile2)
    
data2011 = rawdata2011.dropna()
data2001 = rawdata2001.dropna()

totalDist = set()
totalArea = set()
totalAge = set()

mapDistToRealName = {}
mapData2001 = {}
mapData2001 = defaultdict(lambda:[0]*13, mapData2001)
mapData2011 = {}
mapData2011 = defaultdict(lambda:[0]*13, mapData2011)

for index, row in data2011.iterrows():
    areaName = processAreaName(row['Area Name'])
    totalDist.add(areaName)
    mapDistToRealName[areaName] = row['Area Name']
    totalArea.add(processAreaType(row['Total/Rural/Urban']))
    totalAge.add(processAreaType(row['Present Age']))
    tempList = []
    tempList.append(int(row['Total Women']))
    tempList.append(int(row['Total Ever MarriedWomen']))
    tempList.append(int(row['0']))
    tempList.append(int(row['1']))
    tempList.append(int(row['2']))
    tempList.append(int(row['3']))
    tempList.append(int(row['4']))
    tempList.append(int(row['5']))
    tempList.append(int(row['6']))
    tempList.append(int(row['7+']))
    tempList.append(int(row['Persons']))
    tempList.append(int(row['Males']))
    tempList.append(int(row['Females']))
    key = areaName + '*' + processAreaType(row['Total/Rural/Urban']) + '*' + processAreaType(row['Present Age'])
    mapData2011[key] = tempList
    

for index, row in data2001.iterrows():
    totalDist.add(processAreaName(row['Area Name']))
    totalArea.add(processAreaType(row['Total/Rural/Urban']))
    totalAge.add(processAreaType(row['Present Age']))
    tempList = []
    tempList.append(int(row['Total Women']))
    tempList.append(int(row['Total Ever MarriedWomen']))
    tempList.append(int(row['0']))
    tempList.append(int(row['1']))
    tempList.append(int(row['2']))
    tempList.append(int(row['3']))
    tempList.append(int(row['4']))
    tempList.append(int(row['5']))
    tempList.append(int(row['6']))
    tempList.append(int(row['7+']))
    tempList.append(int(row['Persons']))
    tempList.append(int(row['Males']))
    tempList.append(int(row['Females']))
    key = processAreaName(row['Area Name']) + '*' + processAreaType(row['Total/Rural/Urban']) + '*' + processAreaType(row['Present Age'])
    mapData2001[key] = tempList
    
totalKeys = []
for key,value in mapData2011.items():
    totalKeys.append(key)
for key,value in mapData2001.items():
    totalKeys.append(key)
setKeys = set(totalKeys)

neg = 0
pos = 0
mapRate = {}
for dist in totalDist:
    for area in totalArea:
        for age in totalAge:
            key = dist + '*' + area + '*' +  age
            value2011 = mapData2011[key]
            value2001 = mapData2001[key]
            tempList = []
            for i in range(0 , 13):
                if value2001[i] >= value2011[i]:
                    neg+=1
                else:
                    pos+=1
                if value2001[i] == 0:
                    tempList.append(0)
                else:
                    rate = pow( (value2011[i] / value2001[i]), 0.1) - 1
                    tempList.append(rate)
            mapRate[key] = tempList


fileName = 'Generated Gujrat_district-Total Women,married women, children '
for n in range(7, 11):
    dataList = []
    dataList.append(['Area Name','Total/Rural/Urban','Present Age','Total Women','Total Ever MarriedWomen','0','1','2','3','4','5','6','7+','Persons','Males','Females'])
    for dist in totalDist:
        for area in totalArea:
            for age in totalAge:
                key = dist + '*' + area + '*' +  age
                tempList = []
                tempList.append(dist)
                tempList.append(area)
                tempList.append(age)                
                for j in range(0, 13):
                    P = mapData2001[key][j]
                    r = mapRate[key][j]
                    tempList.append( int( (pow(float(1 + r), n)) * P ) )
                dataList.append(tempList)
    my_df = pd.DataFrame(dataList)
    my_df.to_csv(fileName + str(2000 + n + 1) + '.csv', index=False, header=False)
                

with open("Generated Gujrat_district-Total Women,married women, children 2011.csv") as csvFile3:
    rawdata2011_n = pd.read_csv(csvFile3)
data2011_n = rawdata2011_n.dropna()
mapData2011_n = {}
for index, row in data2011_n.iterrows():
    areaName = processAreaName(row['Area Name'])
    totalDist.add(areaName)
    mapDistToRealName[areaName] = row['Area Name']
    totalArea.add(processAreaType(row['Total/Rural/Urban']))
    totalAge.add(processAreaType(row['Present Age']))
    tempList = []
    tempList.append(int(row['Total Women']))
    tempList.append(int(row['Total Ever MarriedWomen']))
    tempList.append(int(row['0']))
    tempList.append(int(row['1']))
    tempList.append(int(row['2']))
    tempList.append(int(row['3']))
    tempList.append(int(row['4']))
    tempList.append(int(row['5']))
    tempList.append(int(row['6']))
    tempList.append(int(row['7+']))
    tempList.append(int(row['Persons']))
    tempList.append(int(row['Males']))
    tempList.append(int(row['Females']))
    key = areaName + '*' + processAreaType(row['Total/Rural/Urban']) + '*' + processAreaType(row['Present Age'])
    mapData2011_n[key] = tempList

maxDiff = 0;
for key, value in mapData2011_n.items():
    if 'dangs*urban' in key or 'tapi' in key :
        continue
    for i in range(0 ,13):
        nn = mapData2011_n[key][i]
        oo = mapData2011[key][i]
        diff = abs( nn - oo )
        if diff > maxDiff:
            maxDiff = diff
        if diff > 2:
            print(diff)
            print(key)
