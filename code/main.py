from filter import filter_by_specific_values, export_to_csv
import pandas as pd
import matplotlib.pyplot as plt
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


#df = pd.read_csv('batman.csv')
#print(df)
#print(df.info())




#csv_file = 'batman.csv'
#plot_movie_data(csv_file)

# Cargar el archivo CSV en un DataFrame
#df = pd.read_csv('./data/movies.csv', encoding='latin1', delimiter= ';')

# Llamar a la función para graficar los datos
#plot_batman_data(df)


from plotting import plot_movies_by_genre

def main():
    year = 1989
    plot_movies_by_genre(year)

if __name__ == '__main__':
    main()
    
    
    
from genre_and_year import plot_movies_by_genre_and_year

def main():
    direct = 'Woody Allen'

    year = 1981
    plot_movies_by_genre_and_year(direct , year)

if __name__ == '__main__':
    main()










