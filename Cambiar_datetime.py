import pandas as pd

def process_data(df, date_column_name):
    # Convertir la columna de fecha a tipo datetime
    df[date_column_name] = pd.to_datetime(df[date_column_name], errors='coerce')

    # Verificar si hay valores nulos después de la conversión
    if df[date_column_name].isnull().any():
        print("¡Advertencia! Algunos valores en la columna de fecha no son válidos.")

    # Filtrar solo las filas con valores de fecha válidos
    df = df.dropna(subset=[date_column_name])

    # Formatear la columna de fecha como cadenas en el formato YYYY-MM-DD
    df[date_column_name] = df[date_column_name].dt.strftime('%Y-%m-%d')

    # Crear nuevas columnas para Year y Month a partir de la columna de fecha
    df['Año'] = df[date_column_name].str[:4].astype(int)
    df['Mes'] = df[date_column_name].str[5:7].astype(int)
    
    # Agregar una nueva columna con el número de fila de cada celda
    df['Viajes_realizados'] = df.index + 1  # El índice de DataFrame comienza en 0, por eso sumamos 1
    
    return df

def main():
    # Nombre del archivo de entrada y salida
    input_file = '2023_11_parte2_utf8.csv'  # Cambiar al nombre de tu archivo .csv o .xlsx
    output_file = '2023_11_parte2.xlsx'  # Nombre del archivo de salida .xlsx

    # Leer el archivo de entrada
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        df = pd.read_excel(input_file)
    else:
        print("Formato de archivo no compatible. Use un archivo .csv o .xlsx.")
        return

    # Nombre de la columna que contiene la fecha
    date_column_name = 'Fecha_Retiro'  # Cambiar al nombre de tu columna de fecha

    # Procesar los datos sin modificar la columna original de fecha
    df_processed = process_data(df.copy(), date_column_name)

    # Guardar el DataFrame procesado en un nuevo archivo .xlsx
    df_processed.to_excel(output_file, index=False)
    print(f"Archivo procesado guardado como '{output_file}'.")

if __name__ == "__main__":
    main()
