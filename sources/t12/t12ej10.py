import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(3,4), index=['2','1','3'], columns=list('ACBD'))
print(df)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(axis=0, ascending=True))