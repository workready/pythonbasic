import numpy as np
import pandas as pd
s = pd.Series([1,3,5,np.nan,6,8],['A','B','C','D','E','F'])
print(s.A)
print(s['F'])
print(s.dtype)