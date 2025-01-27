import csv
import chardet

def detect_encoding(filename):
    with open(filename, 'rb') as f:
        rawdata = f.read()
    encoding_result = chardet.detect(rawdata)
    return encoding_result['encoding']

filename = '2018-01_Fecha-limpio.csv'
encoding = detect_encoding(filename)

if encoding == 'utf-8':
    print(f"El archivo {filename} está codificado en UTF-8.")
else:
    print(f"El archivo {filename} no está codificado en UTF-8. La codificación detectada es {encoding}.")

output_file = '2018-01_Fecha-limpio_utf8.csv'
