import csv
import codecs

def convert_to_utf8(input_file, output_file):
    # Abrir el archivo CSV en modo lectura con la codificación latin1
    with codecs.open(input_file, 'r', encoding='latin1') as file_in:
        # Leer el archivo CSV
        csv_reader = csv.reader(file_in)
        # Abrir un nuevo archivo CSV en modo escritura con codificación UTF-8
        with codecs.open(output_file, 'w', encoding='utf-8') as file_out:
            # Escribir el contenido en el nuevo archivo UTF-8
            csv_writer = csv.writer(file_out)
            for row in csv_reader:
                csv_writer.writerow(row)

# Especificar el nombre del archivo de entrada y de salida
input_filename = '2018-01_Fecha-limpio.csv'
output_filename = '2018-01_utf8.csv'

# Llamar a la función para convertir el archivo CSV a UTF-8
convert_to_utf8(input_filename, output_filename)

print(f'Archivo convertido a UTF-8: {output_filename}')
