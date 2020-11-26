# -*- coding: utf-8 -*-
import pandas as pd
from os import walk

###################### Edit Distance ###########################

def editDistance(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]

###################### Edit Distance ###########################


himsFiles = "Maharashtra"
f_hims = []
for (dirpath, dirnames, filenames) in walk(himsFiles):
    f_hims.extend(filenames)
    break

censusFiles = "Census/Maharashtra"
f_census = []
for (dirpath, dirnames, filenames) in walk(censusFiles):
    for file in filenames:
        if file.endswith('.csv') and file!="Overall2011.csv" and file!="GujaratOverall2001.csv":
            f_census.append(file)

mappingYR = []
for file1 in f_hims:
    first = file1[11:15]
    print(first)
    tmp =[]
    for file2 in f_census:
        if first in file2:
            tmp.append(himsFiles+"/"+file1)
            tmp.append(censusFiles+ "/"+file2)
            break
    mappingYR.append(tmp)

mappingYR.sort(key = lambda x: x[0])

# print(mappingYR)

listFrames = []
for files in mappingYR:
    file1 = files[0]
    file2 = files[1]
    print(file1+"\n")


    df1 = pd.read_csv(file1,thousands=',')
    df2 = pd.read_csv(file2)

    ############## Renaming the indicator which edit distance can't handle ################
    # df1.loc[df1["Indicator"] == "Leh Ladakh","Indicator"] = "leh(ladakh)"
    # df1.loc[df1["Indicator"] == "Bangalore Urban","Indicator"] = "bangalore"
    df1.loc[df1["Indicator"] == "Brihan Mumbai","Indicator"] = "Mumbai"
    ############## Renaming the indicator which edit distance can't handle ################


    ######################### Removing spaces from the indicator name ##########################
    for i in range(df1.shape[0]):
        str = df1.loc[i,'Indicator'].split(" ")
        mergestr=""
        for k in str:
            mergestr = "".join([mergestr,k])
        df1.loc[i,'Indicator'] = mergestr.lower() #indicator in lower case.
    ######################### Removing spaces from the indicator name ##########################


    ###################### Drop a list of rows from Data Frame ####################
    df1 = df1.iloc[1:] #Dropped first row
    df1.fillna(0,inplace = True)
    column_list = list(df1)
    column_list.remove("Indicator")
    df1 = df1.loc[df1.sum(axis=1)!=0] #dropped the rows which are completely blank.
    newdf1 = df1.copy()
    ###################### Drop a list of rows from Data Frame ####################


    rowHims_file1 = df1['Indicator']
    rowCensus_file2 = df2['Area Name']

    ################# Dist HIMS to Dist Census ###################
    dictHIMStoCensus = dict()

    for i in rowHims_file1:
        l = 3
        include = "No"
        for j in rowCensus_file2:
            # ret = editDistance("s","ddf",5,6)
            ret = editDistance(i,j,len(i),len(j))
            if ret < l:
                l = ret
                include = j
        dictHIMStoCensus[i] = include

    ################# Dist HIMS to Dist Census ###################


    # print(df1)


    #################### Merging Data of Two Files ######################
    df2 = df2.sort_values(by = 'Area Name')
    newdf1 = newdf1.sort_values(by = 'Indicator')
    newdf1 = newdf1.fillna(0)

    # print(newdf1)

    for index in newdf1.index:
        val = dictHIMStoCensus[newdf1['Indicator'][index]]
        newdf1.loc[index,'Indicator']  = val
    print(newdf1)
    finaldf_1 = newdf1.merge(df2, left_on = 'Indicator', right_on = 'Area Name')
    # finaldf_1.to_csv('test.csv', index = False)
    finaldf_1.drop(['Area Name'], axis=1, inplace=True)

    #################### Merging Data of Two Files ######################


    ################### Assign ID to District ##########################
    DistToID = dict()
    start = 1
    for i,row in finaldf_1.iterrows():
        DistToID[row['Indicator']] = start
        start += 1

    for index in finaldf_1.index:
        entry = DistToID[finaldf_1['Indicator'][index]]
        finaldf_1.loc[index,'Indicator']  = entry

    ################### Assign ID to District ##########################

    listFrames.append(finaldf_1)

################## Concatenate the files ###########################
frames  = listFrames
result = pd.concat(frames)
# result['Total Number of Infant Deaths reported'] /= result['Total number of pregnant women Registered for ANC']
# result['Total Number of Infant Deaths reported'] *= 100
# appToEnd = result.pop('Total Number of Infant Deaths reported')
appToEnd = result.pop('Total Number of reported live births')
#appToEnd = result.pop("Total Number of reported Still Births")
print(appToEnd)

# result['Total Number of Infant Deaths reported']=appToEnd
result['Total Number of reported live births']=appToEnd
#result["Total Number of reported Still Births"] = appToEnd


# LIVE BIRTHS
attributes = ["Indicator",
               "Total number of pregnant women Registered for ANC",
               "Number of Pregnant women registered within first trimester",
               "Number of pregnant women received 3 ANC check ups",
               "TT2 or Booster given to Pregnant women (numbers)",
               "Number of Pregnant women given 100 IFA tablets",
              # "Number having Hb level<11 (tested cases)",
              # "Number having severe anaemia (Hb<7) treated at institution",
               "Number of Home deliveries",
               "Number of home deliveries attended by SBA trained (Doctor/Nurse/ANM)",
              # "Number of home deliveries attended by Non SBA trained (trained TB/Dai)",
               "Deliveries Conducted at Public Institutions",
               "Number of Women Discharged under 48 hours of delivery in public facilities",
               "Institutional deliveries (Public Insts.+Pvt. Insts.)",
               "Total reported deliveries",
              # "Number of C-section deliveries conducted at public facilities",
              # "Number of C-section deliveries conducted at private facilities",
#               "Total Number of reported live births",
#               "Total Number of reported Still Births",
               "Number of Newborns having weight less than 2.5 kg",
               "Number of New Borns Breast Fed within 1 hour",
               "Sex Ratio at birth ( Female Live Bitrths/ Male Births *1000)",
#               "Total Number of Abortions ( Spontaneous/ Induced) Reported",
#               "Total Number of MTPs ( Public) reported",
#               "Number of Vasectomies Conducted (Public + Pvt.)",
#               "Number of Tubectomies Conducted (Public + Pvt.)",
#               "Total Sterilisation Conducted",
#               "IUCD Insertions done (public facilities)",
#               "IUCD insertions done (pvt. facilities)",
#               "Oral Pills distributed",
#               "Condom pieces distributed",
               "Number of Infants given OPV 0 (Birth Dose)",
               "Number of Infants given BCG",
              "Number of Infants given DPT1",
              "Number of Infants given DPT2",
               "Number of Infants given DPT3",
               "Number of Infants given Measles",
               "Number of fully immunized children (9-11 months)"
              # "Adverse Events Following Imunisation (Others)",
              # "Number of Major Operations",
              # "Number of Minor Operations",
              # "Total Number of Infant Deaths reported"
#              "Population Persons",
#              "Literate Persons",
#              "Main workers Persons"
#              "Marginal workers Persons",
#              "Non-workers Persons"

              ]

for i in attributes:
    result.pop(i)

result.to_csv("CleanedMaharashtra_8to18.csv",index = False)

################## Concatenate the files ###########################
