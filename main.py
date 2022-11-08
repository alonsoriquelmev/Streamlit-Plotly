import streamlit as st
import pandas as pd
import plotly.express as px

data_games = pd.read_excel('Ventas+Videojuegos.xlsx')
data_transformed = pd.DataFrame()
df_aux = pd.DataFrame()
for index, row in data_games.iterrows():  
        new_row = row[['Nombre','Plataforma','Año','Genero','Editorial']]
        paste_row = pd.DataFrame({'Nombre' : row['Nombre'], 'Plataforma' : row['Plataforma'], 'Año' : row['Año'], 'Genero' : row['Genero'], 'Editorial' : row['Editorial'],
        'Pais': ['NorteAmerica', 'Europa', 'Japon', 'Otros'], 
        'Ventas' : [row['Ventas NA'], row['Ventas EU'], row['Ventas JP'], row['Ventas Otros']]})
        df_aux = pd.concat([df_aux,paste_row], ignore_index = True)

print(df_aux.head(25))
# st.header("Gráficos de Ventas Videojuegos")

# with st.container():
#     fig = px.bar(data_games, x='Plataforma', y = 'Ventas Global', color = '')