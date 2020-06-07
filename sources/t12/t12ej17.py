import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(4,4), index=['a','b','c','d'], columns=list('ABCD'))
df['E'] = ['amarillo','azul','rojo','verde']
print(df)
print()
df[df.E.isin(['rojo','verde'])]=df.loc[:,'A':'D']+10
df[df.A > 0]=df.loc[:,'A':'D']+10
print(df)
