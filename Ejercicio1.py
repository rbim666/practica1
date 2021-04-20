import csv
archivo = open(r"D:\mauro escritorio\Documents\Cosas de la Facultad de Informática\Seminario de Lenguajes\Seminario de Lenguajes Python\Python2021\Actividades\Actividades Teoría\Actividad1_teoria\appstore_games.csv", "r", encoding='utf-8')
csvreader = csv.reader(archivo, delimiter=',')
encabezado = next(csvreader)
print(encabezado)
lista = []
for linea in csvreader:
    if(linea[0] == '0' and linea[13] == 'ES'):
        lista.append(linea[3])
archivo.close()

