import pandas as pd

data_cars = pd.read_csv('Cars.csv', sep=';')

new_data_cars = pd.DataFrame()

# for index, row in data_cars.iterrows():
#         data_aux = row
#         data_aux['MPG'] = str(data_aux['MPG'])
#         new_data_cars = pd.concat([new_data_cars,data_aux], ignore_index=True)
# data_cars['MPG'] = data_cars['MPG'].astype('|S80')
data_cars['MPG'] = data_cars['MPG'].str.replace(',','.').astype(float)
data_cars['Displacement'] = data_cars['Displacement'].str.replace(',','.')
data_cars['Displacement'] = data_cars['Displacement'].str.replace('.0','')
data_cars['Displacement'] = data_cars['Displacement'].str.replace('97.','97').astype(int)
data_cars['Horsepower'] = data_cars['Horsepower'].str.replace(',0','').astype(int)
data_cars['Acceleration'] = data_cars['Acceleration'].str.replace(',','.').astype(float)
data_cars['Fabricante'] = data_cars['Car'].apply(lambda x: x.split(' ')[0])
data_cars['Fabricante'].replace({'Chevrolete' : 'Chevrolet'}, inplace=True)

data_cars['Modelo'] = None
for index, row in data_cars.iterrows():
        fabricante = row['Fabricante']
        data_cars.at[index, 'Modelo'] = row['Car'].replace(fabricante+' ','')

data_cars['YearModel'] = data_cars['Model'].apply(lambda x: 1900+x)



origin = data_cars.Origin.value_counts()
origin_quant = pd.DataFrame(origin)