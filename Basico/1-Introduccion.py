import pandas as pd #importanmos la libreria pandas y le ponemos el apodo pd

df = pd.read_csv('Basico/dataset.csv')#lo convertimos a dataframe 
#

print(df.head(2))#muestra la cantidad de filas que le indiques

print(df.info())#muestra informacion general del dataframe

df2 = pd.read_csv('Basico/fifa_players.csv')

print(df2.info())
'''

print("=== 1. DETECCIÓN DE VALORES NULOS ===")
# isnull().sum() escanea cada columna y suma cuántos datos faltantes hay.
# Es fundamental para saber qué tan "sucio" está nuestro dataset.
print(df.isnull().sum())

print("\n=== 2. LIMPIEZA (IMPUTACIÓN) ===")
# En lugar de borrar a David, vamos a rellenar su edad vacía con el promedio de edad del resto.
# Calculamos el promedio de la columna 'edad'
promedio_edad = df['edad'].mean()
# Rellenamos los vacíos (NaN) con ese promedio
df['edad'] = df['edad'].fillna(promedio_edad)

print("Edades después de la limpieza:")
print(df[['nombre', 'edad']]) # Solo imprimimos estas dos columnas para verificar

print("\n=== 3. FILTRADO (Equivalente a WHERE en SQL) ===")
# Queremos ver ÚNICAMENTE a los empleados del departamento de 'Ventas'
# La condición df['departamento'] == 'Ventas' se envuelve dentro del DataFrame df[...]
ventas_df = df[df['departamento'] == 'Ventas']

print(ventas_df)
'''