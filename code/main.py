from filter import filter_by_specific_values
import pandas as pd
import matplotlib.pyplot as plt
from export import export_to_csv
from plotting import plot_movies_by_genre
#from plotting import plot_batman_data



nombre = './data/movies.csv'
columns_to_filter = ['Genre', 'Year']
values_to_filter = ['Drama', 1981]
filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
print(filter_by_specific_values(nombre, columns_to_filter, values_to_filter))





nombre = './data/movies.csv'
columns_to_filter = ['Genre', 'Year']
values_to_filter = ['Drama', 1981]

dataframeblabla = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)

columns_to_use = ['Name', 'Genre', 'Year']
output_file_name = 'Batman.csv'
print(export_to_csv(dataframeblabla, columns_to_use, output_file_name))


# df = pd.read_csv('batman.csv')

# # Obtener los nombres de las películas y el año
# names = df['Name']
# year = df['Year']

# # Crear la figura y los ejes del gráfico
# fig, ax = plt.subplots(figsize=(11, 6))
# bar_width = 0.5  # Ajusta este valor según tus necesidades

# #obtener los índices para las barras

# # Graficar los datos
# ax.bar(range(len(names)), year, width=bar_width)

# # Configurar los títulos y etiquetas de los ejes
# ax.set_xlabel('Películas')
# ax.set_ylabel('Año 1981')
# ax.set_title('Peliculas por Genero (Drama en 1981)')
# ax.set_xticks(range(len(names)))
# ax.set_xticklabels(names, rotation=45, ha='right')


# Girar las etiquetas del eje x
#plt.xticks(rotation=45)

# Mostrar el gráfico
#plt.show()






from plotting import plot_movies_by_genre

def main():
    year = 1989
    plot_movies_by_genre(year)

if __name__ == '__main__':
    main()
    
    
    
from genre_and_year import plot_movies_by_direct

def main():
    direct = 'James Cameron'
    plot_movies_by_direct(direct )

if __name__ == '__main__':
    main()










