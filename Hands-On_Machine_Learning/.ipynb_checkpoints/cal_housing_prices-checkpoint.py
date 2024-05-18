import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


housing = fetch_california_housing(as_frame=True)
housing = housing.frame
housing.head()

housing.describe()

housing.isnull().sum()

housing.dtypes

housing.hist(bins=50, figsize=(12,8))
plt.show()

housing.plot(kind="scatter", x="Longitude", y="Latitude", c="MedHouseVal", 
             cmap="jet", colorbar=True, legend=True, sharex=False, figsize=(10,7),
             s=housing['Population']/100, label="population", alpha=0.7)
plt.show()


attributes = list(housing.drop(columns=['Latitude', 'Longitude']).columns)
scatter_matrix(housing[attributes], figsize=(12,8))
plt.show()

housing.plot(kind="scatter", x="MedInc", y="MedHouseVal")
plt.show()

corr = housing.corr()
corr['MedHouseVal'].sort_values(ascending=True)

X = housing.iloc[:, :-1]
y = housing.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split()