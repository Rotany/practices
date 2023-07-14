
import pandas as pd
import matplotlib.pyplot as plt
from filter import filter_by_specific_values
from export import export_to_csv
from plotting import plot_movies_by_genre
from budget_and_director import plot_movies_by_direct
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






def main():
    year = 1989
    plot_movies_by_genre(year)

if __name__ == '__main__':
    main()
    
    
    

def main():
    direct = 'James Cameron'
    plot_movies_by_direct(direct )

if __name__ == '__main__':
    main()
    
    
    
    
      #df = pd.read_csv('batman.csv')




nombre = './data/world_population.csv'
columns_to_filter = ['Continent' ]
values_to_filter = ['Europe'  ]
filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
print(filter_by_specific_values(nombre, columns_to_filter, values_to_filter))


nombre = './data/Cien_bancos_mas_grandes.csv'
columns_to_filter = ['Country']
values_to_filter = ['Spain']
filtered_data = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
print(filtered_data)



nombre = './data/world_population.csv'
columns_to_filter = ['Continent']
values_to_filter = ['North America', ]

dataframeblabla = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)

columns_to_use = ['Country','Growth Rate' ]

output_file_name = 'world.csv'
print(export_to_csv(dataframeblabla, columns_to_use, output_file_name))




# Cargar los datos desde el archivo CSV
df = pd.read_csv('world.csv',encoding='latin1', delimiter=',')
print(df)

# Obtener las columnas necesarias para el gráfico de pastel
countries = df['Country']
growth_rates = df['Growth Rate']

# Crear el gráfico de pastel
fig, ax = plt.subplots(figsize=(11, 5))
ax.bar(countries,growth_rates )
plt.xticks(rotation = 45)
ax.set_yticklabels(['{:.1f}%'.format(x * 1) for x in ax.get_yticks()])
#ax.set_ylim(10, max(growth_rates) + 10)
print('hola')
ax.set_xticks(range(len(countries )))
ax.set_xticklabels(countries, rotation=45, ha='right') 


# Agregar título
ax.set_xlabel('Países')
ax.set_ylabel('Tasa de crecimiento')
ax.set_title('Tasa de crecimiento de países')

# Mostrar el gráfico
plt.show()



    
























