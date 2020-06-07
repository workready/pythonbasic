import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10,4), columns=list('ABCD'))
print(df.head())
print(df.tail(2))