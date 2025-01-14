import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

df_match= pd.read_csv("/Users/sangojusaianuragh/Desktop/iplproject/matches.csv")
print(df_match.head())
df_del= pd.read_csv("/Users/sangojusaianuragh/Desktop/iplproject/deliveries.csv")
print(df_del.head())