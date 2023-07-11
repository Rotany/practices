import filter_by_specific_values 
 

import pandas

nombre = './data/movies.csv'
columns_to_filter = ['Genre', 'Year']
values_to_filter = ['Drama', 1981]

new_dataframe = filter_by_specific_values(nombre, columns_to_filter, values_to_filter)
print(new_dataframe)


    
    
    
    
    
    
    
    






    


