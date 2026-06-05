# Importación de librerías. Se utilizan 'np' y 'pd' por convención estándar.
import numpy as np
import pandas as pd

# 1. Definición de los datos
# Usamos un diccionario estándar de Python. Las claves serán los nombres de las columnas, 
# y las listas serán los registros de esa columna.
datos = {
    'id_usuario': [101, 102, 103],
    'edad': [21, 22, np.nan], # np.nan (Not a Number) de NumPy representa un valor nulo o faltante, equivalente a NULL en SQL.
    'rol': ['admin', 'usuario', 'usuario']
}

# 2. Creación del DataFrame
# pd.DataFrame() toma el diccionario y lo convierte en una estructura bidimensional indexada.
df = pd.DataFrame(datos)

# 3. Visualización
# df.head(n) es un método que retorna las primeras 'n' filas del DataFrame.
# Es equivalente a ejecutar un "SELECT * FROM tabla FETCH FIRST n ROWS ONLY".
print(df.head(2))