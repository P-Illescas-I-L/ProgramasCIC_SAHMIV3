import pandas as pd

# 1. Leer el archivo CSV
archivo_csv = 'F:/Datos_Limpios/2023/2023-01.csv'
df = pd.read_csv(archivo_csv)

# 2. Convertir las columnas de fecha de DD/MM/YYYY a YYYY-MM-DD
df['Fecha_Retiro'] = pd.to_datetime(df['Fecha_Retiro'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
df['Fecha_Arribo'] = pd.to_datetime(df['Fecha_Arribo'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

# 3. Guardar el archivo modificado
df.to_csv('F:/Datos_Limpios/2023/2023-01_Fecha.csv', index=False)

# Contar registros modificados y nulos
modificados_retiro = df['Fecha_Retiro'].notna().sum()  # Registros no nulos en 'Fecha_Retiro'
modificados_arribo = df['Fecha_Arribo'].notna().sum()  # Registros no nulos en 'Fecha_Arribo'
nulos_retiro = df['Fecha_Retiro'].isna().sum()  # Registros nulos en 'Fecha_Retiro'
nulos_arribo = df['Fecha_Arribo'].isna().sum()  # Registros nulos en 'Fecha_Arribo'

# Mostrar resultados
print(f"Registros del archivo: {archivo_csv}")
print(f"Registros modificados en 'Fecha_Retiro': {modificados_retiro}")
print(f"Registros modificados en 'Fecha_Arribo': {modificados_arribo}")
print(f"Registros nulos en 'Fecha_Retiro': {nulos_retiro}")
print(f"Registros nulos en 'Fecha_Arribo': {nulos_arribo}")
print("Archivo modificado guardado")
