import pandas as pd

df = pd.read_csv('credit_data.csv')
df.dtypes
df.age.plot()
df.isnull().sum()

a = 1




