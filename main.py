import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('happy.csv')
cols = df.columns

st.title('In Search for Happiness')

x = st.selectbox('Select the data for the X-axis', options=(col.upper() for col in cols))
y = st.selectbox('Select the data for the Y-axis', options=(col.upper() for col in cols))

st.subheader(f'{x} and {y}')


x_data = df[x.lower()]
y_data = df[y.lower()]

figure = px.scatter(x=x_data, y=y_data, labels={'x': x, 'y': y})

st.plotly_chart(figure)
