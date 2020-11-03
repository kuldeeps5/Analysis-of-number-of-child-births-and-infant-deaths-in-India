# -*- coding: utf-8 -*-
'''  
Date: 02-11-2020
@ author Aditya Jain
'''

import pandas as pd;

#Enter input file name without extension
inputname = 'gujarat'
#Enter the previous year
previous_year = "2007-08"
#---------------------------------------------

file = inputname +'.csv'
# df = pd.read_excel(file)
df= pd.read_csv(file)


df.drop(previous_year, axis =1, inplace = True)
for i in range(1,162):
    dropname =  previous_year+ '.' + str(i)
    df.drop(dropname, axis =1 , inplace = True)

df.drop(df.columns[0], axis =1, inplace = True)

column_numbers = [0,1,2,6,7,10,12,13,16,17,18,22,23,25,27,31,32,44,46,50,52,56,62,63,71,72,73,93,94,100,101,103,104,107,108,109,113,115,120,138,139,154]

df = df[df.columns[column_numbers]]

names = "Indicator,Total number of pregnant women Registered for ANC,Number of Pregnant women registered within first trimester,Number of pregnant women received 3 ANC check ups,TT2 or Booster given to Pregnant women (numbers),Number of Pregnant women given 100 IFA tablets,Number having Hb level<11 (tested cases),Number having severe anaemia (Hb<7) treated at institution,Number of Home deliveries,Number of home deliveries attended by SBA trained (Doctor/Nurse/ANM),Number of home deliveries attended by Non SBA trained (trained TB/Dai),Deliveries Conducted at Public Institutions,Number of Women Discharged under 48 hours of delivery in public facilities,Institutional deliveries (Public Insts.+Pvt. Insts.),Total reported deliveries,Number of C-section deliveries conducted at public facilities,Number of C-section deliveries conducted at private facilities,Total Number of reported live births,Total Number of reported Still Births,Number of Newborns having weight less than 2.5 kg,Number of New Borns Breast Fed within 1 hour,Sex Ratio at birth ( Female Live Bitrths/ Male Births *1000),Total Number of Abortions ( Spontaneous/ Induced) Reported,Total Number of MTPs ( Public) reported,Number of Vasectomies Conducted (Public + Pvt.),Number of Tubectomies Conducted (Public + Pvt.),Total Sterilisation Conducted,IUCD Insertions done (public facilities),IUCD insertions done (pvt. facilities),Oral Pills distributed,Condom pieces distributed,Number of Infants given OPV 0 (Birth Dose),Number of Infants given BCG,Number of Infants given DPT1,Number of Infants given DPT2,Number of Infants given DPT3,Number of Infants given Measles,Number of fully immunized children (9-11 months),Adverse Events Following Imunisation (Others),Number of Major Operations,Number of Minor Operations,Total Number of Infant Deaths reported"
names = names.split(",")
df.columns = [names]
# print(df)
output_name = "output_" + inputname + ".csv" 
df.to_csv(output_name, index = False)
print("Ouput File generated - ", end="")
print(output_name)
