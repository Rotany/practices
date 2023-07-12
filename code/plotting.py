import pandas as pd
import matplotlib.pyplot as plt

# def plot_movie_data(csv_file):
#     # Cargar el archivo CSV en un DataFrame
#     df = pd.read_csv(csv_file, encoding='latin1', delimiter= ';')

#     # Graficar los datos
#     plt.plot(df['Name'], df['Genre'])
#     plt.xlabel('Año')
#     plt.ylabel('Recaudación')
#     plt.title('Recaudación de Batman por año')
#     plt.show()
    
    

def plot_batman_data(df):
    # Obtener las columnas necesarias para graficar
    years = df['Year']
    genres = df['Genre']
    
    # Contar la cantidad de películas por género
    genre_counts = genres.value_counts()
    
    # Graficar los datos
    plt.bar(genre_counts.index, genre_counts.values)
    plt.figure(figsize=(10, 6))  # Cambia el tamaño según tus necesidades
    plt.xlabel('Género')
    plt.ylabel('Cantidad de películas')
    plt.title('Distribución de películas de Batman por género')
    plt.xticks(rotation=45)  # Ajusta el ángulo según tus necesidades
    plt.show()





