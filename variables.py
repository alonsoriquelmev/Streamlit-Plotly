from data import data_cars

list_prod = data_cars.Fabricante.unique()
list_years = data_cars.YearModel.unique()
list_years = ['None', *list_years]
list_origin = data_cars.Origin.unique()