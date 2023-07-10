import csv
import codecs

def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, 'r', ) as archivo:
        lector_csv = csv.reader(archivo, delimiter= ';')
        header = next(lector_csv)
        
        
        for row in lector_csv:
            iterable = zip( header, row)
            print(iterable)
            
            
            name_dict ={ key:values for key, values in iterable}
            print(name_dict)

archivo_csv = './data/movies.csv'
datos = leer_archivo_csv(archivo_csv)



    
    
    
    
    
    
    
    






    


