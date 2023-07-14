import pandas as pd
import matplotlib.pyplot as plt
from filter import filter_by_specific_values

def plot_movies_by_direct(direct):
    filtered_df = filter_by_specific_values(file_name= './data/movies.csv',columns_to_filter = ['Director'], values_to_filter = [direct])


    movie_names = filtered_df['Name']
    genres = filtered_df['Genre']

    # Crear la figura y los ejes del gráfico con un tamaño más grande
    fig, ax = plt.subplots(figsize=(11, 11))  # Ajusta el tamaño según tus necesidades
    bars = ax.bar(movie_names, filtered_df['Budget'], width=0.6)
    unique_genres = genres.unique()

    # Crear un diccionario para mapear géneros a colores
    genre_colors = {
        'Action': 'red',
        'Comedy': 'blue',
        'Drama': 'green',
        'Crime': 'yellow',
        'Horror': 'green',
        'Adventure': 'purple',
        'Biography': 'gray',
        'Animation': 'pink',
        'Fantasy': 'orange'
        # Agrega más géneros y colores según tus necesidades
    }
    # Agregar leyendas al gráfico
    for i, bar in enumerate(bars):
        
        genre = genres.iloc[i]
        bar.set_color(genre_colors[genre])
        #rear leyendas para cada género
    legend_labels = [plt.Rectangle((0, 0), 1, 1, color=genre_colors[genre]) for genre in unique_genres]
    ax.legend(legend_labels, unique_genres)



    # Graficar los datos
    ax.set_xticks(range(len(movie_names)))
    ax.set_xticklabels(movie_names, rotation=45, ha='right') 
    ax.set_xlabel('Películas')
    ax.set_ylabel('Presupuesto')
    ax.set_title(f'Presupuesto De Películas Por Director {direct}')
    

    # Girar las etiquetas del eje x
    plt.xticks(rotation=45)  # Ajusta el ángulo según tus necesidades
    
    plt.show()
    
    
    

