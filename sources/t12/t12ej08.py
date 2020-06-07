import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(3,4), index=['2','4','8'], columns=list('ABCD'))
print(df.describe())