import pandas as pd

df = pd.read_csv('Basico/fifa_players.csv', encoding='latin1') #latin1 para tildes y ñ


#print(df.isnull().sum()) #sumar todos los valores nulos de cada columna

print(df['age'].mean()) #muestra el promedio de edad 

nacionalidad = df[df['nationality'] == 'Ecuador'] #creamos un dataframe, buscamos en nacionalidad sea Ecuatorianos 

print(nacionalidad['name']) #muestras elk campo name de nuestro nuevo dataframe 