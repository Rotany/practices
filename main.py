import csv
import codecs

def leer_archivo_csv(nombre_archivo):
    with codecs.open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.reader(archivo, delimiter= ';')
        
        
        header = next(lector_csv)
        for row in lector_csv:
            iterable = zip( header, row)
            
            name_dict = {key: values for key, values in iterable}
            print(name_dict)

archivo_csv = './data/movies.csv'
datos = leer_archivo_csv(archivo_csv)


    
    
    
    
    
    
    
    






    


