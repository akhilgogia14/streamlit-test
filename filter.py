import pandas as pd
from pathlib import Path  


df = pd.read_csv('export (1).csv')
df = df.loc[df['Player'] != "Player"]

df.to_csv('nba.csv', encoding='utf-8', index=False)


print(df)
