import pandas as pd
from numpy.ma.core import std

df = pd.Series([15,18,19,20,20,20,21,23,23,24,24,25,45,30,33,37,21,38,42,49,50])
print(df)

mean = df.mean()
print(mean)

median = df.median()
print(median)

mode =df.mode()
print(mode)

Variance = df.var()
print(Variance)

std = df.std(ddof=0)
print(std)
