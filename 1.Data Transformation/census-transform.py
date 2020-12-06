'''
Date: 01-11-2020
@ author Aditya Jain
'''

import pandas as pd;
import os

############################### Tranforming Census 2001 Files ##########################################

mainFolder = "All States Census 2001 Unprocessed xls files"
arr = []
for d,r,f in os.walk(mainFolder):
    for name in f:
        arr.append(name)



for file in sorted(arr):
    #Reading the excel file using xlrd package
    df = pd.read_excel(mainFolder + '/' + file)

    # dropping rural and urban rows
    df = df[df['TRU']=="Total"]
    df = df[["NAME", 'TOT_P','P_LIT', 'MAINWORK_P', 'MARGWORK_P', 'NON_WORK_P']]
    df.columns = ['Area Name', 'Population Persons','Literate Persons','Main workers Persons','Marginal workers Persons','Non-workers Persons']

    # dropping first 3 irrelevant rows
    df = df.loc[3:]

    split = file.split(".")
    outputfile = "All States Census 2001 Processed csv files/" + split[0] + ".csv"
    df.to_csv(outputfile, index = False)
    print("Output File Generated: " , end= "")
    print(outputfile)

############################### Tranforming Census 2001 Files ##########################################




############################### Tranforming Census 2011 Files ##########################################

mainFolder = "All States Census 2011 Unprocessed xls files"
arr = []
for d,r,f in os.walk(mainFolder):
    for name in f:
        arr.append(name)


for file in sorted(arr):
    #Reading the excel file using xlrd package
    df = pd.read_excel(mainFolder + '/' + file)

    # dropping rural and urban rows
    df = df[df['TRU']=="Total"]
    df = df[["Name", 'TOT_P','P_LIT', 'MAINWORK_P', 'MARGWORK_P', 'NON_WORK_P']]
    df.columns = ['Area Name', 'Population Persons','Literate Persons','Main workers Persons','Marginal workers Persons','Non-workers Persons']

    # dropping first 3 rows
    df = df.loc[3:]

    split = file.split(".")
    outputfile = "All States Census 2011 Processed csv files/" + split[0] + "2011" + ".csv"
    df.to_csv(outputfile, index = False)
    print("Output File Generated: " , end= "")
    print(outputfile)

############################### Tranforming Census 2011 Files ##########################################
