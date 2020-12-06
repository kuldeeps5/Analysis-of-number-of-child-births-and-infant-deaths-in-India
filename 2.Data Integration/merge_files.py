'''
@ author Aditya Jain
'''

import pandas as pd;
import os

mainFolder = "MergedFiles"
arr = []
for d,r,f in os.walk(mainFolder):
    for name in f:
        arr.append(mainFolder + '/' + name)

# print(len(arr))

df = pd.DataFrame()

# Reading and merging all csv files into one dataframe df
for i in sorted(arr):
    print(i)
    df1 = pd.read_csv(i)
    df = pd.concat([df,df1], ignore_index = True)
# print(df)

# Outputing the merged dataframe.
df.to_csv("all_states_merged_8to18.csv", index = False)

# df1 = pd.read_csv(arr[0])
# df1 = pd.read_csv(arr[1])
# print(df1)
