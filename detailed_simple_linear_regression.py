# -*- coding: utf-8 -*-
"""Detailed Simple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dNd6-S2CmYoz61kU0Ynz-cWey_G1etyG
"""

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Importing the dataset
dataset = pd.read_csv("covid_data.csv")

dataset.head

dataset.columns

dataset.info()

dataset.describe()

dataset.count()

dataset.describe

# Selecting a numeric column for simplicity (you can choose a different one)
selected_column = 'gdp_per_capita'

# Extracting features (X) and target variable (y)
X = dataset[[selected_column]].values
y = dataset['new_cases'].values

# Handling missing values in X
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature scaling (optional, but often beneficial for linear regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Fitting simple linear regression to the training set
regressor = LinearRegression()
regressor.fit(X_train_scaled, y_train)

# Predicting the test set results
y_pred = regressor.predict(X_test_scaled)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Visualizing the results
plt.scatter(X_test_scaled, y_test, color='blue', label='Actual values')
plt.plot(X_test_scaled, y_pred, color='red', linewidth=2, label='Regression line')
plt.title(f'Simple Linear Regression: {selected_column} vs. new_cases')
plt.xlabel(selected_column)
plt.ylabel('new_cases')
plt.legend()
plt.show()

