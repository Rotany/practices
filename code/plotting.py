import pandas as pd
import matplotlib.pyplot as plt


# grafico correcto 
def plot_movies_by_genre(year):

     df = pd.read_csv('./data/movies.csv', encoding= 'latin1', delimiter= ';')

# Convertir la columna 'Year' a tipo numérico
     df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Filtrar los datos por el año 1989
     filtered_df = df[df['Year'] == 1989]

# Obtener la cantidad de películas por género
     genre_counts = filtered_df['Genre'].value_counts()

# Crear la figura y los ejes del gráfico
     fig, ax = plt.subplots(figsize=(10, 6))  # Ajusta el tamaño según tus necesidades

# Graficar los datos
     genre_counts.plot(kind='bar', ax=ax, color= ['blue','red','green', 'pink','yellow', 'orange','purple','gray'])
     ax.set_xlabel('Género')
     ax.set_ylabel('Cantidad de películas')
     ax.set_title('Cantidad de películas por género en 1989')
     ax.set_xticklabels(genre_counts.index, rotation=45, ha='right')

     plt.xticks(rotation=45) 
     plt.show()





