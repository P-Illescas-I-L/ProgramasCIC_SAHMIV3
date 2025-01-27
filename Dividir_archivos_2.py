#Dividir_archivos_2
import csv

def split_csv_file(input_file, num_files):
    # Crear una lista de nombres para los archivos de salida
    output_files = [f'archivo_unido_parte{i+1}.csv' for i in range(num_files)]
    
    # Abrir todos los archivos de salida en modo escritura
    with open(input_file, 'r', newline='') as infile:
        readers = csv.reader(infile)
        
        # Crear un diccionario de escritores CSV para cada archivo de salida
        writers = {}
        for i, output_file in enumerate(output_files):
            outfile = open(output_file, 'w', newline='')
            writers[i] = csv.writer(outfile)

        # Leer la cabecera del archivo CSV (si existe)
        header = next(readers)
        for writer in writers.values():
            writer.writerow(header)

        # Distribuir las líneas del archivo original en los archivos de salida
        for i, row in enumerate(readers):
            current_writer = writers[i % num_files]
            current_writer.writerow(row)

        # Cerrar todos los archivos de salida
        for outfile in writers.values():
            outfile.writerow([])

    print(f"Archivo CSV dividido en {num_files} partes.")

# Uso: especifica el nombre del archivo de entrada y el número de archivos de salida
input_file = 'Consulta_viajesporaym.csv'
num_files = 6  # Número de archivos de salida

split_csv_file(input_file, num_files)
