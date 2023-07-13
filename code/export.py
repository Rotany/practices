import pandas as pd

def export_to_csv(dataframe, columns_to_use, output_file_name):
     # Crear un nuevo DataFrame con las columnas seleccionadas
    selected_columns = dataframe[columns_to_use]
    
    # Exportar el DataFrame a un archivo CSV
    selected_columns.to_csv(output_file_name, index=False)
    # devolvemos el DataFrame que vamos a exportar
    return selected_columns