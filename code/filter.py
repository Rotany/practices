import csv
import pandas as pd



def filter_by_specific_values(file_name, columns_to_filter, values_to_filter):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(file_name, encoding='latin1', delimiter= ';')
    
    # Filtrar el DataFrame usando los valores y columnas especificados
    filtered_df = df[df[columns_to_filter[0]] == values_to_filter[0]]
    for i in range(1, len(columns_to_filter)):
        filtered_df = filtered_df[filtered_df[columns_to_filter[i]] == values_to_filter[i]]
    
    # Devolver el DataFrame filtrado
    return filtered_df[columns_to_filter]




    # def filter_by_specific_values(file_name, columns_to_filter, values_to_filter):
#     # Verificar la longitud de las listas
#     if len(columns_to_filter) != len(values_to_filter):
#         raise Exception("Por favor, 'columns_to_filter' y 'values_to_filter' deben tener la misma longitud.")
    
#     # Cargar el archivo CSV en un DataFrame
#     df = pd.read_csv(file_name, encoding='latin1', delimiter= ';')
    
#     # Filtrar el DataFrame usando los valores y columnas especificados
#     filtered_df = df.copy()
#     for column, value in zip(columns_to_filter, values_to_filter):
#         filtered_df = filtered_df[filtered_df[column] == value]
    
    # Devolver el DataFrame filtrado
    #return filtered_df
# nombre = './data/movies.csv'
# columns_to_filter = ['Genre', 'Year']
# values_to_filter = ['Drama', 1981]

# filtered_data = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
# print(filtered_data)



# def filter_by_specific_values(file_name, columns_to_filter, values_to_filter):
#     # Cargar el archivo CSV en un DataFrame
#     df = pd.read_csv(file_name,encoding= 'latin1', delimiter= ';')
    
#     # Filtrar el DataFrame usando los valores y columnas especificados
#     filtered_df = df[df[columns_to_filter[0]] == values_to_filter[0]]
#     for i in range(1, len(columns_to_filter)):
#         filtered_df = filtered_df[filtered_df[columns_to_filter[i]] == values_to_filter[i]]
    
#     # Devolver el DataFrame filtrado
#     return filtered_df




def filter_by_specific_values(file_name, columns_to_filter, values_to_filter):
    # Cargar el archivo CSV en un DataFrame, saltando la primera línea como encabezado
    df = pd.read_csv(file_name, encoding='latin1', delimiter=';', header=0)

    # Filtrar el DataFrame usando los valores y columnas especificados
    filtered_df = df.copy()
    for column, value in zip(columns_to_filter, values_to_filter):
        filtered_df = filtered_df[filtered_df[column] == value]

    # Devolver el DataFrame filtrado
    return filtered_df






















    
    
    



     

    

    


    







