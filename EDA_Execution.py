import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
file_path = r'C:\Users\Hp\OneDrive\Pictures\Desktop\Projects\Python\Neet_Result_2024.csv'
data = pd.read_csv(file_path)
#data

#To display the information of the dataset
data.info()
data.head()
print("\nSummary of the dataset: \n",data.describe())
print("\nColumn Names:\n", data.columns)
print("\nUnique Values:\n ",data.nunique())  #use to count unique values.


#Handling the missing data
print("\nMissing Values in Each Column:\n",data.isnull().sum())
print("\nIf null values, then fill with NaN: \n", data.dropna())
