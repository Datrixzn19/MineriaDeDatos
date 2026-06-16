import pandas as pd

df = pd.read_csv('Basico/fifa_players.csv', encoding='latin1') #latin1 para tildes y ñ


#print(df.isnull().sum()) #sumar todos los valores nulos de cada columna

print(df['age'].mean()) 

nacionalidad = df[df['nationality'] == 'Ecuador']

print(nacionalidad['name'])