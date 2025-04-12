import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file_path = r'C:\Users\Hp\OneDrive\Pictures\Desktop\Projects\Python\Neet_Result_2024.csv'
df = pd.read_csv(file_path)

#To display the information of the dataset
df.info()
df.head()
print("\nSummary of the dataset: \n",df.describe())
print("\nColumn Names:\n", df.columns)
print("\nUnique Values:\n ",df.nunique())  #use to count unique values.

#Handling the missing data
print("\nMissing Values in Each Column:\n",df.isnull().sum())
print("\nIf null values, then fill with NaN: \n", df.dropna())


#Objective 1: Analyze the average and median marks of students across 
#different states to determine which states performed above or below the
#national average.

# One row per state (state-level values are repeated)
states = df.drop_duplicates(subset="state")

# Creating hue column 
states["Performance"] = states["state_average_marks"] > states["national_average_marks"]

# Sort states by average marks
states = states.sort_values("state_average_marks", ascending=False)

# Ploting bar graph
plt.figure(figsize=(8, 6))
sns.barplot(data=states, x="state", y="state_average_marks", hue="Performance", palette="viridis")
plt.title("State Average NEET Marks vs National Average", fontsize=14)
plt.xlabel("State")
plt.ylabel("Average Marks")
plt.xticks(rotation=90)
plt.legend(title="Above National Avg", loc="upper right")
plt.tight_layout()
plt.show()


#Objective 2: Visualize the distribution of states based on the number
#of students scoring above 600 and 700 using histograms, to understand
#how high scorers are spread across states.

df = df.drop_duplicates(subset="state")

# Ploting both histograms
plt.figure(figsize=(8, 6))
sns.histplot(df["above_600_marks"], color="pink", label="Above 600", bins=15, kde=False)
sns.histplot(df["above_700_marks"], color="blue", label="Above 700", bins=15, kde=False)
plt.title("Distribution of States by Number of High Scorers")
plt.xlabel("Number of Students")
plt.ylabel("Number of States")
plt.legend()
plt.show()
