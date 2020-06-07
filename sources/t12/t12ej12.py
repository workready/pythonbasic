
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(4,4), index=['a','b','c','d'], columns=list('ABCD'))
print(df)
print()
print(df[0:2])
print()
print(df['A'][2])
print()
print(df.A.b)
