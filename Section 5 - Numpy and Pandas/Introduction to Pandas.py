# Natural Language Processing using Python

# Introduction to pandas
# Importing Libraries
import pandas as pd
import numpy as np

# Series
# pd.Series(self, data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

x = pd.Series([1,2,3,4,5])

x + 100

(x ** 2) + 100

x > 2


# any and all
larger_than_2 = x > 2

larger_than_2.any()

larger_than_2.all()

# apply
def f(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return x ** 3

x.apply(f)

# Converting types
x.astype(np.float64)

# Copy
x
y = x
y[0] = 100

x = pd.Series([1,2,3,4,5])
y = x.copy()

y[0] = 100
y

# Dataframes
# pd.DataFrame(self, data=None, index=None, columns=None, dtype=None, copy=False)

data = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(data, columns=["x"])
df

# One column as a series
dataSeries = df["x"]

# Adding more columns
df["x_plus_2"] = df["x"] + 2
df

df["x_square"] = df["x"] ** 2
df["x_factorial"] = df["x"].apply(np.math.factorial)
df

df["is_even"] = df["x"] % 2
df

# Dropping/Deleting columns
df = df.drop("is_even", 1)
df

# Selecting multiple columns
df[["x","x_plus_2"]]

# Describing
df.describe()


# Reading datasets
dataset = pd.read_csv('matches.csv')