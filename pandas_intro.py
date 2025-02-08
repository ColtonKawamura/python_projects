import pandas as pd
import numpy as np


# -------- Step 1, create a DataFrame to Work with -------------

# create a 5 row, 3 column array with randomon interegers
np.random.seed(42) # set the seed so it's random, but replicable
data = np.random.randint(1,100, (5,3)) # (start, stop, (row, column))
print(data)

# now we turn this into a DataFrame, very useful aspect of pandas (long with a series)
df = pd.DataFrame(data, columns =['A', 'B', 'C'])
print(df)

# -------- Step 2, Create a new column based on others -------------
# Let's create a new column D = A + B - C

df["D"] = df["A"]+df["B"]-df["C"]

# -------- Step 3, Save it as a .CSV -------------

df.to_csv("data.csv", index=False) # index = False prevents an extra column called "Unnamed" from being saved
df = pd.read_csv("data.csv")
print(df)

# -------- Step 4, Grab some stats -------------
print("\nDataFrame mean:\n",df.mean())
print("\nDataFrame min:\n",df.max())


# -------- Step 5, Do a T-Test -------------
from scipy import stats

t_stat, p_value = stats.ttest_ind(df["A"], df["B"])

print("\nT-Test Results (A vs B):")
print("T-Statistic:", t_stat) # How much the means of groups differ relative to the spread of their data.
print("P-Value:", p_value) # If p-value < 0.05, A and B have significantly different means.
