#Limpieza_completa
#Control de errores
#..............................................
# El programa añade una columna llamada unnamed:9 que se tiene que eliminar 
#..............................................

import pandas as pd

# Leer el archivo CSV (con la extensión)
archivo_csv = '2018-12.csv'
df = pd.read_csv(archivo_csv)

df = pd.read_csv(archivo_csv)

# Contar el número total de registros antes de hacer cualquier cambio
total_registros_antes = len(df)

# Contar los registros antes de eliminar nulos
n_registros_antes = df.shape[0]

# Conteo de los nulos encontrados en cada columna
nulos_antes_edad = df["Edad_Usuario"].isna().sum()
nulos_antes_bici = df["Bici"].isna().sum()
nulos_antes_genero = df["Genero_Usuario"].isna().sum()
nulos_antes_FechaR = df["Fecha_Retiro"].isna().sum()
nulos_antes_FechaA = df["Fecha_Arribo"].isna().sum()




# Se eliminan las filas con datos vacíos en las columnas especificadas
df.dropna(subset=["Edad_Usuario", "Bici", "Genero_Usuario", "Fecha_Retiro", "Fecha_Arribo"], inplace=True)

# Contar los registros después de eliminar nulos
n_registros_despues = df.shape[0]

# Imprimir cuántos registros fueron eliminados
registros_eliminados = n_registros_antes - n_registros_despues

#-------------------------------------------------------------------------------
#Cambiar el formato de las fechas
#-------------------------------------------------------------------------------

#Cambio de formato de fecha
df["Fecha_Retiro"] = pd.to_datetime(df["Fecha_Retiro"], format="mixed")
df["Fecha_Arribo"] = pd.to_datetime(df["Fecha_Arribo"], format="mixed")

# Contar registros modificados y nulos
modificados_retiro = df['Fecha_Retiro'].notna().sum()  # Registros no nulos en 'Fecha_Retiro'
modificados_arribo = df['Fecha_Arribo'].notna().sum()  # Registros no nulos en 'Fecha_Arribo'
nulos_retiro = df['Fecha_Retiro'].isna().sum()  # Registros nulos en 'Fecha_Retiro'
nulos_arribo = df['Fecha_Arribo'].isna().sum()  # Registros nulos en 'Fecha_Arribo'

#-------------------------------------------------------------------------------
#Eliminar no númericos de Bici
#-------------------------------------------------------------------------------
# Contar el número de filas antes de la limpieza
filas_antes_bici = len(df)

# Convertir la columna 'Bici' a numérico, convirtiendo caracteres a NaN
df['Bici'] = pd.to_numeric(df['Bici'], errors='coerce')

# Eliminar filas con NaN en la columna 'Bici'
df = df.dropna(subset=['Bici'])


# Contar el número de filas después de la limpieza
filas_despues = len(df)

# Calcular el número de registros modificados (eliminados)
registros_modificados = filas_antes_bici - filas_despues

#-------------------------------------------------------------------------------
#Eliminar cicloestaciones con mas de un registro
#-------------------------------------------------------------------------------


# Crear copias de las columnas originales para compararlas más tarde
original_arribo = df['Ciclo_Estacion_Arribo'].copy()
original_retiro = df['Ciclo_Estacion_Retiro'].copy()

# Definir la función para reemplazar los valores
def replace_value(value):
    if isinstance(value, str) and '-' in value:
        return value.split('-')[0]
    elif isinstance(value, int):  # Agregar manejo para valores enteros
        return str(value)  # Convertir el entero a una cadena de texto
    else:
        return value

# Aplicar la función para reemplazar los valores en las mismas columnas
df['Ciclo_Estacion_Arribo'] = df['Ciclo_Estacion_Arribo'].apply(replace_value)
df['Ciclo_Estacion_Retiro'] = df['Ciclo_Estacion_Retiro'].apply(replace_value)

# Contar cuántos registros fueron modificados en cada columna
modificados_arribo = (original_arribo != df['Ciclo_Estacion_Arribo']).sum()
modificados_retiro = (original_retiro != df['Ciclo_Estacion_Retiro']).sum()


#-------------------------------------------------------------------------------
#Verificar Horarios
#-------------------------------------------------------------------------------

# Convertir las columnas a datetime (asumiendo que el formato es 'YYYY-MM-DD HH:MM:SS')
df['Hora_Retiro'] = pd.to_datetime(df['Hora_Retiro'], format='%H:%M:%S', errors='coerce')
df['Hora_Arribo'] = pd.to_datetime(df['Hora_Arribo'], format='%H:%M:%S', errors='coerce')

# Extraer la hora y verificar si está fuera del rango 0-23
retiro_fuera_de_rango = df[df['Hora_Retiro'].dt.hour.notnull() & ~df['Hora_Retiro'].dt.hour.between(0, 23)]
arribo_fuera_de_rango = df[df['Hora_Arribo'].dt.hour.notnull() & ~df['Hora_Arribo'].dt.hour.between(0, 23)]

#++++++++++++++++++++++++++++++MODIFICAR+++++++++++++++++++++++++++++++++++++++++++++++++++++
# Extraer la hora y verificar si está fuera del rango 0-23
retiro_fuera_de_rango = df[df['Fecha_Retiro'] < pd.Timestamp ('2015-01-01')]
arribo_fuera_de_rango = df[df['Fecha_Arribo'] < pd.Timestamp ('2015-01-01')]
#++++++++++++++++++++++++++++++MODIFICAR+++++++++++++++++++++++++++++++++++++++++++++++++++++

# Formatear las columnas para mostrar solo la hora en formato 'HH:MM:SS'
df['Hora_Retiro'] = df['Hora_Retiro'].dt.strftime('%H:%M:%S')
df['Hora_Arribo'] = df['Hora_Arribo'].dt.strftime('%H:%M:%S')

# Contar cuántos registros tienen horas fuera del rango en cada columna
retiro_count = retiro_fuera_de_rango.shape[0]
arribo_count = arribo_fuera_de_rango.shape[0]

#------Importante modificar antes de ejecutar--------------
# Guardar el archivo modificado
df.to_csv('D:/Users/ianlu/OneDrive/SAHMI_Datos/2018/Datos_Descargados/2018-12_Limpio.csv', index=False)
#------Importante modificar antes de ejecutar--------------



with open(f'resultados_limpieza_{archivo_csv}.txt', 'w') as f:
  print(f"Nombre del archivo: {archivo_csv}")
  print(f"Total de registros antes de cambios: {total_registros_antes}", file=f)
  print(f"Registros del archivo: {archivo_csv}")
  print(f'Se eliminaron {registros_eliminados} registros.', file=f)
  print(f"Registros modificados en 'Fecha_Retiro': {modificados_retiro}", file=f)
  print(f"Registros modificados en 'Fecha_Arribo': {modificados_arribo}", file=f)
  print(f"Registros nulos en 'Fecha_Retiro': {nulos_retiro}", file=f)
  print(f"Registros nulos en 'Fecha_Arribo': {nulos_arribo}", file=f)
  print(f"Registros modificados en 'Ciclo_EstacionArribo': {modificados_arribo}", file=f)
  print(f"Registros modificados en 'Ciclo_Estacion_Retiro': {modificados_retiro}",file=f)  
  print(f"Registros con horas fuera del rango en Hora_Retiro: {retiro_count}", file=f)
  print(f"Registros con horas fuera del rango en Hora_Arribo: {arribo_count}", file=f)
  print(f"Se eliminaron {registros_modificados} registros no numéricos de la columna 'Bici'.", file=f)