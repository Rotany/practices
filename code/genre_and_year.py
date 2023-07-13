import pandas as pd
import matplotlib.pyplot as plt

def plot_movies_by_direct(direct):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv('./data/movies.csv', encoding= 'latin1', delimiter=';')

    # Filtrar los datos por género y año
    filtered_df = df[(df['Director'] == direct)]

    # Obtener los nombres de las películas
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
    #ax.set_xticks(x_indices)
    ax.set_xticklabels(movie_names, rotation=45, ha='right') 
    ax.set_xlabel('Películas')
    ax.set_ylabel('Presupuesto')
    ax.set_title(f'Presupuesto De Películas Por Director {direct}')
    

    # Girar las etiquetas del eje x
    plt.xticks(rotation=45)  # Ajusta el ángulo según tus necesidades
    
    plt.show()

