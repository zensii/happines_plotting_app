import streamlit as st
import plotly.express as px

st.title('In Search for Happiness')

x = st.selectbox('Select the data for the X-axis', options=('Option1', 'Option2'))
y = st.selectbox('Select the data for the Y-axis', options=('Option1', 'Option2'))

st.subheader(f'{x} and {y}')

x_data = [5,12,25,67,88]
y_data = [12,14,16,17,43]
figure = px.scatter(x=x_data, y=y_data , labels={'x': x, 'y': y})

st.plotly_chart(figure)