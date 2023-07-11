from filter import filter_by_specific_values
from filter import filter_by_specific_values, export_to_csv
import pandas

#nombre = './data/movies.csv'
#columns_to_filter = ['Genre', 'Year']
#values_to_filter = ['Drama', 1981]
#filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
#print(filter_by_specific_values(nombre, columns_to_filter, values_to_filter))





nombre = './data/movies.csv'
columns_to_filter = ['Genre', 'Year']
values_to_filter = ['Drama', 1981]

dataframeblabla = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)

columns_to_use = ['Name', 'Genre', 'Year']
output_file_name = 'batmaqan.csv'

export_to_csv(dataframeblabla, columns_to_use, output_file_name)