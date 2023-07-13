
import pandas as pd
import matplotlib.pyplot as plt
from filter import filter_by_specific_values
from export import export_to_csv
from plotting import plot_movies_by_genre
from budget_and_director import plot_movies_by_direct
#from plotting import plot_batman_data



# nombre = './data/movies.csv'
# columns_to_filter = ['Genre', 'Year']
# values_to_filter = ['Drama', 1981]
# filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
# print(filter_by_specific_values(nombre, columns_to_filter, values_to_filter))





# nombre = './data/movies.csv'
# columns_to_filter = ['Genre', 'Year']
# values_to_filter = ['Drama', 1981]

# dataframeblabla = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)

# columns_to_use = ['Name', 'Genre', 'Year']
# output_file_name = 'Batman.csv'
# print(export_to_csv(dataframeblabla, columns_to_use, output_file_name))






# def main():
#     year = 1989
#     plot_movies_by_genre(year)

# if __name__ == '__main__':
#     main()
    
    
    

# def main():
#     direct = 'James Cameron'
#     plot_movies_by_direct(direct )

# if __name__ == '__main__':
#     main()
    
    
    
    
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



# nombre = './data/world_population.csv'
# columns_to_filter = ['Country/Territory', '2022 Population']
# values_to_filter = ['Afghanistan',41128771 ]
# filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
# print(filter_by_specific_values(nombre, columns_to_filter, values_to_filter))


nombre = './data/Cien_bancos_mas_grandes.csv'
columns_to_filter = ['Country']
values_to_filter = ['Spain']
filtered_data = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
print(filtered_data)



nombre = './data/Cien_bancos_mas_grandes.csv'
columns_to_filter = ['Country']
values_to_filter = ['Spain']

dataframeblabla = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)

columns_to_use = ['Bank name', 'Country']
output_file_name = 'Bancos.csv'
print(export_to_csv(dataframeblabla, columns_to_use, output_file_name))























