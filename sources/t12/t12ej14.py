import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(4,4), index=['a','b','c','d'], columns=list('ABCD'))
print(df)
print()
print(df.iloc[1])
print()
print(df.iloc[:,[1,3]])
print()
print(df.iloc[0:2])
print()
print(df.iloc[1,2])
print()
print(df.iat[1,2])
