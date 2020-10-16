# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import pandas as pd
from os import walk

############################# FEATURE SET #####################################
attributes = ["Indicator",
              "Total number of pregnant women Registered for ANC",
              "Number of Pregnant women registered within first trimester",
              "Number of pregnant women received 3 ANC check ups",
              "TT2 or Booster given to Pregnant women (numbers)",
              "Number of Pregnant women given 100 IFA tablets",
              "Number having Hb level<11 (tested cases)",
              "Number having severe anaemia (Hb<7) treated at institution",
              "Number of Home deliveries",
              "Number of home deliveries attended by SBA trained (Doctor/Nurse/ANM)",
              "Number of home deliveries attended by Non SBA trained (trained TB/Dai)",
              "Deliveries Conducted at Public Institutions",
              "Number of Women Discharged under 48 hours of delivery in public facilities",
              "Institutional deliveries (Public Insts.+Pvt. Insts.)",
              "Total reported deliveries",
              "Number of C-section deliveries conducted at public facilities",
              "Number of C-section deliveries conducted at private facilities",
              "Total Number of reported live births",
              "Total Number of reported Still Births",
              "Number of Newborns having weight less than 2.5 kg",
              "Number of New Borns Breast Fed within 1 hour",
              "Sex Ratio at birth ( Female Live Bitrths/ Male Births *1000)",
              "Total Number of Abortions ( Spontaneous/ Induced) Reported",
              "Total Number of MTPs ( Public) reported",
              "Number of Vasectomies Conducted (Public + Pvt.)",
              "Number of Tubectomies Conducted (Public + Pvt.)",
              "Total Sterilisation Conducted",
              "IUCD Insertions done (public facilities)",
              "IUCD insertions done (pvt. facilities)",
              "Oral Pills distributed",
              "Condom pieces distributed",
              "Number of Infants given OPV 0 (Birth Dose)",
              "Number of Infants given BCG",
              "Number of Infants given DPT1",
              "Number of Infants given DPT2",
              "Number of Infants given DPT3",
              "Number of Infants given Measles",
              "Number of fully immunized children (9-11 months)",
              "Adverse Events Following Imunisation (Others)",
              "Number of Major Operations",
              "Number of Minor Operations",
              "Total Number of Infant Deaths reported"]
############################# FEATURE SET #####################################


###################### Dealing with exact attribute match #####################
mypath = "Data/Modified/Gujarat/p1/"

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

for i in f:
    if i.endswith('.csv'):
        df = pd.read_csv(mypath + i)
        df.dropna(thresh=1, inplace = True)
        original = df.columns
        df = df[attributes]
        df.to_csv("ModifiedData/Gujarat/"+i,columns = attributes,index = False)
        
###################### Dealing with exact attribute match #####################
        

############### Dealing with Edit Distance attribute match ####################
def editDistance(str1, str2, m, n): 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0: 
                dp[i][j] = j 
            elif j == 0: 
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1], 
                                   dp[i-1][j],   
                                   dp[i-1][j-1])   
  
    return dp[m][n]
############### Dealing with Edit Distance attribute match ####################
    
################################# Processing ##################################

mypath = "Data/Modified/Gujarat/p2/"

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

dictMappingEdit = dict()
dictMappingEdit["TT2 or Booster given to Pregnant women (numbers)"] = \
            "TT2 given to Pregnant women (numbers)"
dictMappingEdit["Number of Pregnant women given 100 IFA tablets"] = \
            "Number of Pregnant women given 180 IFA tablets"
dictMappingEdit["Total Number of Abortions ( Spontaneous/ Induced) Reported"]=\
            "Total Number of Abortions ( Spontaneous) Reported"
dictMappingEdit["Total Number of MTPs ( Public) reported"] = \
            "Total Number of MTPs ( Public) conducted"
dictMappingEdit["Number of pregnant women received 3 ANC check ups"] =\
            "Number of pregnant women received 4 or more ANC check ups"
            
################################# Processing ##################################
            

######################## 2017-18 Data #########################################
df = pd.read_csv(mypath + f[1])
original = df.columns
modifiedAttr = []
for i in attributes:
    if i in dictMappingEdit:
        modifiedAttr.append(dictMappingEdit[i])
    else:
        l = 10000000
        include = ""
        for j in original:  
            ret = editDistance(str(i),str(j),len(i),len(j))
            if ret < l:
                l = ret
                include = str(j)
        modifiedAttr.append(include)
df = df[modifiedAttr]
df.columns = attributes    
df.to_csv("ModifiedData/Gujarat/"+f[1],columns = attributes,index = False)
######################## 2017-18 Data #########################################


######################## 2018-19 Data #########################################
df = pd.read_csv(mypath + f[2])
original = df.columns
modifiedAttr = []
for i in attributes:
    if i in dictMappingEdit:
        modifiedAttr.append(dictMappingEdit[i])
    else:
        l = 10000000
        include = ""
        for j in original:  
            ret = editDistance(str(i),str(j),len(i),len(j))
            if ret < l:
                l = ret
                include = str(j)
        modifiedAttr.append(include)
df = df[modifiedAttr]
df.columns = attributes    
df.to_csv("ModifiedData/Gujarat/"+f[2],columns = attributes,index = False)
######################## 2018-19 Data #########################################


######################### Validation ##########################################
#mynewpath = "ModifiedData/Gujarat/"
#f1 = []
#for (dirpath, dirnames, filenames) in walk(mynewpath):
#    f1.extend(filenames)
#    break
#
#for i in f1:
#    if i.endswith('.csv'):
#        df = pd.read_csv(mynewpath + i)
#        if df.columns != attributes:
#            print("false")
        
######################### Validation ##########################################        
        
        
        
        
        
        
        
        
        



