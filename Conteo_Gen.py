import csv

def contar_letras_en_columna(archivo_csv, columna_index):
    # Definir el conjunto de letras que queremos contar
    letras_a_contar = {'M', 'F', 'O'}
    
    # Contador para cada letra
    conteo_letras = {'M': 0, 'F': 0, 'O': 0}
    
    with open(archivo_csv, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        # Saltar la primera fila (encabezado)
        next(reader)
        
        # Iterar sobre cada fila del archivo CSV
        for row in reader:
            if len(row) > columna_index:  # Verificar que la fila tenga suficientes columnas
                # Obtener el valor de la columna específica
                valor_columna = row[columna_index]  # No se elimina ningún espacio en blanco
                
                # Contar las ocurrencias de las letras en el valor de la columna
                for letra in letras_a_contar:
                    conteo_letras[letra] += valor_columna.count(letra)
            else:
                # Si la fila no tiene suficientes columnas, contar como celda vacía
                conteo_letras[''] += 1
    
    return conteo_letras

# Uso: especificar el nombre del archivo CSV y el índice de la columna (0 para la primera columna)
archivo_csv = '2023_09_parte2_utf8.csv'
columna_index = 0  # Primera columna (índice 0 en base cero)

# Llamar a la función para contar las letras en la columna especificada
resultado_conteo = contar_letras_en_columna(archivo_csv, columna_index)

# Imprimir el resultado del conteo
print("Número de ocurrencias de las letras (incluidas celdas vacías) en la columna:")
for letra, conteo in resultado_conteo.items():
    print(f"{letra if letra else 'Celda vacía'}: {conteo}")
