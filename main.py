import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import variables as var
from data import data_cars, data_sum
st.set_page_config(page_title = "Classic Cars Dashboard", page_icon = ":car:", layout = 'wide')

st.header('Classic Cars Dataset Dashboard')
st.write('Hi! This is a Dashboard of the Classic Cars dataset from Kaggle.com. We are using Plotly in this case.')

st.sidebar.header("Options")

year_select = st.sidebar.selectbox('Select year', var.list_years)

origin_select = st.sidebar.multiselect('Select origin', var.list_origin, var.list_origin)

list_prod_main = var.list_prod
if len(origin_select) == 1:
    list_prod_main = data_cars[data_cars['Origin'] == origin_select[0]].Fabricante.unique()

fab_select = st.sidebar.multiselect('Select producer', list_prod_main, list_prod_main)

if str(year_select) != 'None':
    data_filtered = data_cars[data_cars['YearModel'] == int(year_select)]
    data_sum = data_sum[data_sum['Year'] == year_select]
else:
    data_filtered = data_cars.copy()

if len(fab_select) >= 1:
    data_filtered = data_filtered[data_filtered['Fabricante'].isin(fab_select)]
else:
    pass

if len(origin_select) >= 1:
    data_filtered = data_filtered[data_filtered['Origin'].isin(origin_select)]
else:
    pass

origin = data_filtered.Origin.value_counts()
origin_quant = pd.DataFrame(origin)

column1, column2 = st.columns(2)
with column1:
    with st.container():
            st.markdown('### Country of origin')
            fig1 = go.Figure(go.Treemap(labels = origin_quant.index, parents = ['Origin', 'Origin', 'Origin'], values = origin_quant.Origin.to_list(), marker_colors= ['#F58523','#B428D0','#2898D0']))
            st.plotly_chart(fig1, use_container_width=True)
with column2:
    with st.container():
        if len(data_filtered.Origin.unique()) == 1:
            st.markdown('### Horsepower vs MPG (By producer)'+' for '+data_filtered.Origin.unique()[0]+' cars')
            fig = px.scatter(data_filtered, x='Horsepower', y='MPG', color = 'Fabricante', hover_data = ['Modelo'], height=600)

        else:
            st.markdown('### Horsepower vs MPG (By country of origin)')
            fig = px.scatter(data_filtered, x='Horsepower', y='MPG', color = 'Origin', hover_data = ['Fabricante','Modelo'], height=600, color_discrete_sequence=['#F58523','#B428D0','#2898D0'])
            
        
        fig.update_traces(marker=dict(size=8,
                                    line=dict(width=1.5)),
                                    opacity = 0.80,
                                    selector=dict(mode='markers'))
        st.plotly_chart(fig, use_container_width=True)

with st.container():
    st.markdown("### Number of cars per year by manufacturing country")
    fig = px.bar(data_sum, x = 'Year', y = 'Count', color = 'Origin', color_discrete_sequence=['#F58523','#B428D0','#2898D0'])
    st.plotly_chart(fig, use_container_width=True)

column1, column2 = st.columns(2)

with column1:
    with st.container():
        if len(fab_select) == 1:
            st.markdown("### Boxplot of MPG of "+str(fab_select[0])+" Cars")
            color_boxplot = var.prod_colors[fab_select[0]]
            fig = px.box(data_filtered, x= 'Fabricante', y = 'MPG', color='Origin', color_discrete_sequence=[color_boxplot])
             
            st.plotly_chart(fig, use_container_width=True)

        else:
            with st.container():
                st.markdown("### Violin plot of MPG of cars by Origin")
                boxplot_select = st.radio("Add box plot to violin chart?", ('Yes','No'), key = 'selectradio1')
                if str(boxplot_select) == 'Yes':
                    
                    fig = px.violin(data_cars, x= 'Origin', y = 'MPG', color='Origin', box = True,color_discrete_sequence=['#F58523','#B428D0','#2898D0'])
                     
                    st.plotly_chart(fig, use_container_width=True)
                elif str(boxplot_select) == 'No':
                    fig = px.violin(data_cars, x= 'Origin', y = 'MPG', color='Origin', box = False, points = 'all',color_discrete_sequence=['#F58523','#B428D0','#2898D0'])
                     
                    st.plotly_chart(fig, use_container_width=True)
with column2:
    with st.container():
        if len(fab_select) == 1:
            st.markdown("### Boxplot of Horsepower of "+str(fab_select[0])+" Cars")
            color_boxplot = var.prod_colors[fab_select[0]]
            fig = px.box(data_filtered, x = 'Origin', y = 'Horsepower',color='Origin', color_discrete_sequence=[color_boxplot].reverse())
             
            st.plotly_chart(fig, use_container_width=True)
        else:
            with st.container():
                st.markdown("### Violin plot of Horsepower of cars by Origin")
                boxplot_select = st.radio("Add box plot to violin chart?", ('Yes','No'), key = 'selectradio2')
                if str(boxplot_select) == 'Yes':
                    fig = px.violin(data_cars, x = 'Origin', y = 'Horsepower',color='Origin', box = True,color_discrete_sequence=['#F58523','#B428D0','#2898D0'])
                     
                    st.plotly_chart(fig, use_container_width=True)
                elif str(boxplot_select) == 'No':
                    fig = px.violin(data_cars, x = 'Origin', y = 'Horsepower',color='Origin', box = False, points = 'all', color_discrete_sequence=['#F58523','#B428D0','#2898D0'])
                     
                    st.plotly_chart(fig, use_container_width=True)