from data import data_cars
import plotly.express as px

list_prod = data_cars.Fabricante.unique()
list_years = data_cars.YearModel.unique()
list_years = ['None', *list_years]
list_origin = data_cars.Origin.unique()

origin_colors = {'US' : '#F58523', 'Europe' : '#B428D0', 'Japan': '#2898D0'}
colors_palette = px.colors.qualitative.Safe + px.colors.qualitative.Pastel + px.colors.qualitative.Bold
prod_colors = dict(zip(list_prod, colors_palette))