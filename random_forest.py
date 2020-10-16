# -*- coding: utf-8 -*-
# imporiting libraries
import matplotlib.pyplot as plt 
import pandas as pd 
#from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 


# importing database
data = pd.read_csv('CleanedGujarat_8to18.csv')

#dividing the data into dependent and independent variables
# x = data.drop(['Total Number of Infant Deaths reported'], axis=1)
x = data.drop(['Total Number of reported live births'], axis=1)
#x = data.drop(['Total Number of reported Still Births'], axis=1)
# y = data['Total Number of Infant Deaths reported']
y = data['Total Number of reported live births']
#y = data['Total Number of reported Still Births']

# create regressor object of Random Forest 
regressor = RandomForestRegressor(n_estimators = 25,random_state = 0) 

# dividing data into test and train set
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.09,shuffle=False)
  
# fit the regressor with x and y data 
regressor.fit(train_x, train_y)  

y_pred = regressor.predict(test_x)

test_yLIST = list(test_y)
for i in range(len(test_yLIST)):
    print(test_yLIST[i],"<--->",y_pred[i])

# print(max(abs(test_yLIST - y_pred)))
# print(len(test_yLIST))
    
impactData = []
impactData.append(test_yLIST)    
impactData.append(list(y_pred))
for i in range(0,2):
    test_pred = plt.plot(impactData[i])
    test_pred = plt.xlabel('Districts')
    # test_pred = plt.ylabel('Deaths')
    test_pred = plt.ylabel('Births')
plt.legend(['Actual','Predicted'])
plt.savefig('RandomForestLiveBirth.jpg')
plt.show()

print('Training Accuracy : ',regressor.score(train_x,train_y)*100)
print('Testing Accuracy : ',regressor.score(test_x,test_y)*100)

print(regressor.feature_importances_)
values1 = regressor.feature_importances_
values2 = train_x.columns
listValues = []
for i in range(len(values1)):
    tmp = []
    tmp.append(values1[i])
    tmp.append(values2[i])
    listValues.append(tmp)

listValues.sort(key = lambda x:x[0],reverse = True)

for i in range(10):
    print(listValues[i][1])

#fn=list(x.columns)
#cn=['Total Number of Infant Deaths reported']
#fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=1600)
#tree.plot_tree(regressor.estimators_[0],
#                feature_names = fn,
#                class_names=cn,
#                filled = True);
#fig.savefig('rf_individualtree.png')
#
# print("Features sorted by their score:")
# print(sorted(zip(map(lambda x: round(x, 4), regressor.feature_importances_), fn),
#              reverse=True))



