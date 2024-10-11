import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('datos.csv')

# Mostrar las primeras 5 filas del DataFrame
print("Primeras 5 filas del DataFrame:")
print(df.head())

# Descripción estadística del DataFrame
print("\nDescripción estadística del DataFrame:")
print(df.describe())

# Filtrar datos: seleccionar filas donde una columna específica cumple una condición
filtro = df[df['columna'] > valor]
print("\nFiltrado de datos:")
print(filtro)

# Agrupar datos por una columna y calcular la media
agrupado = df.groupby('columna_grupo').mean()
print("\nDatos agrupados por 'columna_grupo' y calculando la media:")
print(agrupado)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('datos_modificados.csv', index=False)
print("\nDatos guardados en 'datos_modificados.csv'")
