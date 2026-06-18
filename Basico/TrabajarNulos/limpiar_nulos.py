#usamos isnull().sum() revisa cada columna y cuenta el total de nulos 

import pandas as pd
import numpy as np

df = pd.read_csv('Basico/fifa_players.csv', encoding='latin1')

print(df.isnull().sum())