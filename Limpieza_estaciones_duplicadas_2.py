#Limpieza_estaciones_duplicadas_2
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('2024-05_parte1-limpio.csv')

# Crear copias de las columnas originales para compararlas más tarde
original_arribo = df['Ciclo_EstacionArribo'].copy()
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
df['Ciclo_EstacionArribo'] = df['Ciclo_EstacionArribo'].apply(replace_value)
df['Ciclo_Estacion_Retiro'] = df['Ciclo_Estacion_Retiro'].apply(replace_value)

# Contar cuántos registros fueron modificados en cada columna
modificados_arribo = (original_arribo != df['Ciclo_EstacionArribo']).sum()
modificados_retiro = (original_retiro != df['Ciclo_Estacion_Retiro']).sum()

# Guardar los cambios en un nuevo archivo CSV
df.to_csv('2024-05-1_parte1_cleaned.csv', index=False)

# Mostrar el número de registros modificados
print(f"Registros modificados en 'Ciclo_EstacionArribo': {modificados_arribo}")
print(f"Registros modificados en 'Ciclo_Estacion_Retiro': {modificados_retiro}")
print("Archivo modificado guardado")
