import pandas as pd
import matplotlib.pyplot as plt

def plot_movies_by_genre_and_year(direct, year):
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv('./data/movies.csv', encoding= 'latin1', delimiter=';')

    # Filtrar los datos por género y año
    filtered_df = df[(df['Director'] == direct)]

    # Obtener los nombres de las películas
    movie_names = filtered_df['Name']

    # Crear la figura y los ejes del gráfico con un tamaño más grande
    fig, ax = plt.subplots(figsize=(11, 11))  # Ajusta el tamaño según tus necesidades
    #sorted_df = filtered_df.sort_values('Budget')
    #x_indices = range(len(movie_names))


    # Graficar los datos
    ax.bar(movie_names,filtered_df['Budget'], width= 0.6)
    #ax.set_xticks(x_indices)
    ax.set_xticklabels(movie_names, rotation=45, ha='right') 
    ax.set_xlabel('Películas')
    ax.set_ylabel('Presupuesto')
    ax.set_title(f'Películas Por Director {direct}, {year}')

    # Girar las etiquetas del eje x
    plt.xticks(rotation=45)  # Ajusta el ángulo según tus necesidades
    
    plt.show()

