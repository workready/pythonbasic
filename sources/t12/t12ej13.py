import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(4,4), index=['a','b','c','d'], columns=list('ABCD'))
df = pd.DataFrame(np.random.randn(4,4), index=['a','b','c','d'], columns=list('ABCD'))
print(df)
print()
print(df.loc['b'])
print()
print(df.loc[:,['A','B']])
print()
print(df.loc['b':'d'])
print()
print(df.loc['b','B'])
print()
print(df.at['b','B'])
