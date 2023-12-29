import pandas as pd
from pathlib import Path  


df = pd.read_csv('/Users/akhilgogia/Documents/export (1).csv')
df = df.loc[df['Player'] != "Player"]

df.to_csv('/Users/akhilgogia/Documents/nba.csv', encoding='utf-8', index=False)


print(df)
