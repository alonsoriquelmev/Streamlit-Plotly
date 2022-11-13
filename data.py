import pandas as pd

data_cars = pd.read_csv('Cars.csv', sep=';')

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

data_aux_sum = data_cars[['Origin','YearModel']]

data_sum = pd.DataFrame(columns=['Origin','Year','Count'])

for origin_type in data_cars.Origin.unique():
        for year in data_cars.YearModel.unique():
                data_aux = data_aux_sum[(data_aux_sum['Origin'] == origin_type) & (data_aux_sum['YearModel'] == year)]
                count = data_aux.shape[0]
                data_join = pd.DataFrame({'Origin': [origin_type],'Year': [year], 'Count':[count]})
                data_sum = pd.concat([data_sum,data_join], ignore_index = True)

