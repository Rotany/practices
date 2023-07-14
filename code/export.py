import pandas as pd

def export_to_csv(dataframe, columns_to_use, output_file_name):
    # Crear un nuevo DataFrame con las columnas seleccionadas
    df_selected_columns = dataframe[columns_to_use]
    
    # Exportar el DataFrame a un archivo CSV
    df_selected_columns.to_csv(output_file_name, index=False)
    # devolvemos el DataFrame que vamos a exportar
    return df_selected_columns