import numpy as np
import pandas as pd
import os

input_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fichero.csv')
df = pd.read_csv(input_file, header = None)    # <1>
print(df.head())