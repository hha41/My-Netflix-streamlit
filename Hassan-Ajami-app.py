import streamlit as st
import numpy as np
import pandas as pd
import scipy as sp
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
from PIL import Image

st.title('Hassan Ajami\'s First Application')

def load_data():
    data = pd.read_csv('netflix_titles.csv')
    return data
netflix_data = load_data()

image = Image.open('netflix.jpg')
st.image(image)

mov_type = st.sidebar.selectbox('Sort by:',['TV Show','Movie'])
mov_Dur = st.sidebar.selectbox('Duration:',['Shortest', 'Longest'])
year=st.sidebar.slider("YEAR",1925,2021,2021)
n= st.sidebar.number_input('Numer of Recommendations', min_value=0, max_value=20, value=10, step=1, format=None, key=None)


best_year=netflix_data[netflix_data['release_year']==year]
best_type=best_year[best_year['type']==mov_type]
st.subheader(f'Top {n} {mov_type} sorted by {mov_Dur} in {year}')
if mov_Dur == 'Shortest':
    dur_sort=best_type.sort_values(['time'],ascending=True).head(n)
else:
    dur_sort=best_type.sort_values(['time'],ascending=False).head(n)

if len(dur_sort) == 0:
    st.write("There are no available options!")
else:
    if n<= len(dur_sort):
        dur_sort.index = pd.RangeIndex(start=1, stop=n+1, step=1)
        st.table(dur_sort)
    else:
        n=len(dur_sort)
        dur_sort.index = pd.RangeIndex(start=1, stop=n+1, step=1)
        st.table(dur_sort)


st.subheader('Duration distribution of film type')
option = st.selectbox('Which film type would you like to analize?', ['TV Show','Movie'])
#hist_duration = np.histogram(netflix_data[netflix_data['type']==option].time, bins = 10)[0]
#st.bar_chart(hist_duration)

fig = px.scatter(netflix_data[netflix_data['type']==option], x="release_year", y="time",                  labels={
                     "release_year": "Release Year",
                     "time": "Duration (Seasons or Minutes)",
                 },hover_data=['title'])
st.plotly_chart(fig)



@st.cache
def load_data2():
    data = pd.read_csv('hopsital_locations_england.csv')
    return data
hosp_data = load_data2()

mapbox_access_token = 'pk.eyJ1IjoiaWhlMTEiLCJhIjoiY2tsM2djcjF1MGkwMjJwcjF4cG4xYjYxbiJ9.dUDnDUmhf2MrVDXmCkOBsg'

data = [
    go.Scattermapbox(
        lat=hosp_data['Latitude'],
        lon=hosp_data['Longitude'],
        mode='markers',
        marker=dict(
            size=5,
            color="red",
            opacity=0.7
        ),
        text=hosp_data.Name,
        hoverinfo='text'
    )]


layout = go.Layout(
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=52,
            lon=-2
        ),
        pitch=0,
        zoom=4,
        style='light'
    ),
)

fig = go.Figure(data=data, layout=layout)

st.subheader('Map of all Hospitals in England')
st.plotly_chart(fig)

