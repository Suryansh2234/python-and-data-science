import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.subheader('Car Crash Data Insights and Visualizations')
st.markdown('Get all the insights as stats and visuals on Car Crash Data.')

st.subheader('Dataset')

df = sns.load_dataset('car_crashes')
st.dataframe(df)

#filters
st.sidebar.header('Filters')
st.sidebar.subheader('Filter by Abbreviation')
abbrev = st.sidebar.multiselect('Select Abbreviations', options=df['abbrev'])
if abbrev:
    df = df[df['abbrev'].isin(abbrev)]

st.subheader('Visuals of Insights')

#age distribution

fig = px.pie(df, values='speeding', names='abbrev', title='Speeding Distribution')
fig.update_traces(textposition='inside')
st.plotly_chart(fig)


