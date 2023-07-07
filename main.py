import csv
import codecs

def leer_archivo_csv(nombre_archivo):
    with codecs.open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.DictReader(archivo)
        datos = [fila for fila in lector_csv]
    return datos
    

archivo_csv = './data/movies.csv'
datos = leer_archivo_csv(archivo_csv)

for fila in datos:
    diccionario_fila = {llave: valor for llave, valor in fila.items()}
    print(diccionario_fila)
    break
    
    
    
    
    
    
    
    






    


