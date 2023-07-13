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
    
    

# def plot_batman_data(df):
#     # Obtener las columnas necesarias para graficar
#     #years = df['Gross']
#     genres = df['Genre']
    
#     # Contar la cantidad de películas por género
#     genre_counts = genres.value_counts()
#     plt.figure(figsize=(10, 6))  # Cambia el tamaño según tus necesidades
    
#     # Graficar los datos
#     plt.bar(genre_counts.index, genre_counts.values)
#     plt.xlabel('Género')
#     plt.ylabel('Cantidad de películas')
#     plt.title('Distribución de películas de Batman por género')
#     plt.xticks(rotation=45)  # Ajusta el ángulo según tus necesidades
#     plt.show()

    

# # Cargar el archivo CSV en un DataFrame
# df = pd.read_csv('./data/movies.csv', encoding= 'latin1', delimiter=';')
# filtered_df = df[df['Year'] == 1989]

# # Obtener las columnas necesarias para graficar
# genres = filtered_df['Genre']
# gross = filtered_df['Gross' ]

# # Crear la figura y los ejes del gráfico
# fig, ax = plt.subplots(figsize=(10, 6))  # Ajusta el tamaño según tus necesidades

# # Graficar los datos
# ax.bar(genres, gross)
# ax.set_xlabel('Years')
# ax.set_ylabel('Recaudación')
# ax.set_title('Presupuesto de películas por género')

# # Girar las etiquetas del eje x
# plt.xticks(rotation=45)  # Ajusta el ángulo según tus necesidades
# plt.yticks(rotation=45)

# plt.show()



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
     genre_counts.plot(kind='bar', ax=ax)
     ax.set_xlabel('Género')
     ax.set_ylabel('Cantidad de películas')
     ax.set_title('Cantidad de películas por género en 1989')
     plt.xticks(rotation=45) 
     plt.show()

if __name__ == '__main__':
     year = 1989
     plot_movies_by_genre(year)


# df = pd.read_csv('./data/movies.csv', encoding= 'latin1', delimiter=';')

# # Filtrar por género 'Drama' y año 1981
# filtered_df = df[(df['Genre'] == 'Action') & (df['Year'] == 2000)]

# # Obtener los nombres de las películas
# movie_names = filtered_df['Name']

# # Crear la figura y los ejes del gráfico
# fig, ax = plt.subplots(figsize=(12, 12))  # Ajusta el tamaño según tus necesidades

# # Graficar los datos
# ax.bar(movie_names, filtered_df['Gross'])
# ax.set_xlabel('Películas')
# ax.set_ylabel('Recaudación')
# ax.set_title('Recaudación de películas de Drama en 1981')

# # Girar las etiquetas del eje x
# plt.xticks(rotation=45)  # Ajusta el ángulo según tus necesidades

# plt.show()





