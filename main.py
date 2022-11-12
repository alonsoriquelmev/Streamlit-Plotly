import streamlit as st
import plotly.express as px
from data import data_cars, origin_quant
import plotly.graph_objects as go

st.set_page_config(page_title = "Classic Cars Dashboard", page_icon = ":car:")

st.header('Classic Cars Dataset Dashboard')
st.write('Hi! This is a Dashboard of the Classic Cars dataset from Kaggle.com. We are using Plotly in this case.')


with st.container():
    st.markdown('### Horsepower vs MPG (By country of origin)')
    fig = px.scatter(data_cars, x='Horsepower', y='MPG', color = 'Origin')
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    st.markdown('### Country of origin')
    fig1 = go.Figure(go.Treemap(labels = origin_quant.index, parents = ['Origin', 'Origin', 'Origin'], values = origin_quant.Origin.to_list()))
    st.plotly_chart(fig1, use_container_width=True)