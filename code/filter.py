import csv
import codecs

def leer_archivo_csv(nombre_archivo):
    with codecs.open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
        lector_csv = csv.DictReader(archivo)
        datos = [fila for fila in lector_csv]
    return datos

def filter_by_specific_values(nombre, columns_to_filter, values_to_filter):
    archivo_csv = f'./data/movies.csv'
    datos = leer_archivo_csv(archivo_csv)
    
    resultados_filtrados = []
    for fila in datos:
        cumple_criterio = True
        for columna, valor in zip(columns_to_filter, values_to_filter):
            if fila[columna] != valor:
                cumple_criterio = False
                break
        if cumple_criterio:
            diccionario_fila = {llave: valor for llave, valor in fila.items()}
            resultados_filtrados.append(diccionario_fila)
    
    return resultados_filtrados
    print(resultados_filtrados)
    
nombre = "data"
columns_to_filter =['genre', 'year']
values_to_filter = ['Drama','1980']

resultados = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
print(resultados)
#for resultado in resultados:
     #print(resultado)





    
    
