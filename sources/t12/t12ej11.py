import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(4,4), index=['1','2','3','4'], columns=list('ABCD'))
print(df)
print(df.sort_values(by='B'))