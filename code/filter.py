import csv
# import codecs
# def leer_archivo_csv(nombre_archivo):
#     with open(nombre_archivo, 'r',   ) as archivo:
#         lector_csv = csv.reader(archivo, delimiter= ';')
#         header = next(lector_csv)  # Saltar la primera línea
#         for row in lector_csv:
#             iterable = zip(header, row)
        
#             datos = {key: values for key , values in iterable}
#             print(datos)
            
           
    
# def filter_by_specific_values(nombre, columns_to_filter, values_to_filter):
#     if len(columns_to_filter) != len(values_to_filter):
        
#          archivo_csv = './data/movies.csv'
#          datos_csv = leer_archivo_csv(archivo_csv)
         
#          resultados_filtrados = []
#          for fila in datos_csv:
#             cumple_criterio = True
#             for columna, valor in zip(columns_to_filter, values_to_filter):
#               print(datos_csv)
            
#             cumple_criterio = False
            
#         if cumple_criterio:
#             diccionario_fila = {llave: valor for llave, valor in fila.items()}
#             resultados_filtrados.append(diccionario_fila)
#     return resultados_filtrados
# nombre = "data"
# columns_to_filter = ['Genre', 'Year']
# values_to_filter = ['Drama', '1980']
# try:
#     resultados = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
#     for resultado in resultados:
#         print(resultado)
# except ValueError as error:
#     print(str(error))

# import pandas as pd

# datos = pd.read_csv('./data/movies.csv')
# print(datos)



# def filter_by_specific_values(file_name, filter_columns, filter_values):
#     filtered_data = []
    
#     with open(file_name, 'r', newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter= ';')
#         for row in reader:
#             # Verificar si las columnas de filtro y sus valores coinciden en la fila actual
#             if all(row[column] == int(value) for column, value in zip(filter_columns, filter_values)):
#                 filtered_data.append(row)
                
    
#     return filtered_data

# # Ejemplo de uso
# file_name = './data/movies.csv'
# filter_columns = ['Name', 'Year']
# filter_values = ['Monkey', '1995']
# filtered_movies = filter_by_specific_values(file_name, filter_columns, filter_values)

# # Imprimir las películas filtradas
# for movies in filtered_movies:
#     print(movies['Name'])
    
    
    
# def filter_movies_by_genre_and_year(file_name, genre, year):
#     filtered_movies = []
    
#     with open(file_name, 'r', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row['Genre'] == genre and row['Year'] == year:
#                 filtered_movies.append(row)
    
#     return filtered_movies

# # Ejemplo de uso
# file_name = './data/movies.csv'
# genre = 'Comedy'
# year = '1992'

# filtered_movies = filter_movies_by_genre_and_year(file_name, genre, year)

# # Imprimir las películas filtradas
# for movie in filtered_movies:
#     print(movie['Name'])



import pandas as pd



archivo_csv = './data/movies.csv'
datos = pd.read_csv(archivo_csv, encoding='latin1', delimiter= ';')

#print(datos.head())  # Imprimir las primeras filas del archivo




# Filtrar por "Genre" y "Year"

def filter_by_specific_values(file_name, filter_columns, filter_values):

filtro_name = datos['Genre'] == 'Drama'
filtro_year = datos['Year'] == 1981
datos_filtrados = datos.loc[filtro_name & filtro_year]
print(datos_filtrados)


    







