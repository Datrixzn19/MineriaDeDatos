import pandas as pd #importanmos la libreria pandas y le ponemos el apodo pd

df = pd.read_csv('Basico/dataset.csv')#lo convertimos a dataframe 
#

print(df.head(2))#muestra la cantidad de filas que le indiques

print(df.info())#muestra informacion general del dataframe
