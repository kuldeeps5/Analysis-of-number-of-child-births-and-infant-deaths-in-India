# -*- coding: utf-8 -*-
#Importing libraries
import pandas as pd

from sklearn.linear_model import LinearRegression

from sklearn.linear_model import Ridge

from sklearn.linear_model import Lasso

df = pd.read_csv('CleanedGujarat_8to18.csv')

# X = df.drop('Total Number of Infant Deaths reported', axis=1)
X = df.drop('Total Number of reported live births', axis=1)

#y = df['Total Number of Infant Deaths reported']
y = df['Total Number of reported live births']


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, shuffle=False)

regression_model = LinearRegression()

regression_model.fit(X_train, y_train)
#
#print(X_train)

pred = regression_model.predict(X_test)
#print(pred)

ridge = Ridge(alpha=0.01)

ridge.fit(X_train,y_train)

print ("Ridge model:", (ridge.coef_))

lasso = Lasso(alpha=0.01)

lasso.fit(X_train,y_train)

#print ("Lasso model:", (lasso.coef_))

print("Linear Regression Model Training Score: ", regression_model.score(X_train, y_train))

print("Linear Regression Model Testing Score: ",regression_model.score(X_test, y_test))

print("Ridge Regression Model Training Score: ",ridge.score(X_train, y_train))

print("Ridge Regression Model Testing Score: ",ridge.score(X_test, y_test))

print("Lasso Regression Model Training Score: ",lasso.score(X_train, y_train))

print("Lasso Regression Model Testing Score: ",lasso.score(X_test, y_test))