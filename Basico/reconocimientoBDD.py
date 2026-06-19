import pandas as pd

df = pd.read_csv('Basico/fifa_players.csv', encoding='latin1') #latin1 para tildes y ñ

#print(df.info()) #informacion de la tabla 

#print(df.head(2)) #muestra las primeras n filas 


print(df.iloc[1]) #muestra un registro en especifico
"""
subtabla = df[['name', 'age']] #trae la subtabla con solo las columnas name y age
print(subtabla.tail(3)) #trae los n ultims registros, se puede ver si la tabla esta compoleta 
"""