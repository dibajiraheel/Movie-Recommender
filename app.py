# Import Libraries
import pandas as pd
import numpy as np
import pickle
import ast
import streamlit as st
import requests


# Load Dataframe
df = pickle.load(open('Recommended.pkl','rb'))
df = pd.DataFrame(df)

# Function to fetch poster
# --------------https://api.themoviedb.org/3/movie/297761?api_key=eec045e46b32c82150532de6ad756605-----------
def poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=eec045e46b32c82150532de6ad756605'.format(id))
    data = response.json()
    poster_path = 'https://image.tmdb.org/t/p/original/' + data['poster_path']
    return poster_path
    

# Recommendation function
def recommend_genres(movie):
    
    title = []
    poster_path = []

    id = list(df[df['title'] == movie]['Recommended_genres'])[0]
    
    for i in range(len(id)):
        title.append(list(df[df['id'] == id[i]]['title'])[0])
    
    for i in range(len(title)):
        poster_path.append(poster(id[i]))
    return title,poster_path

def recommend_actors(movie):
    
    title = []
    poster_path = []

    id = list(df[df['title'] == movie]['Recommended_actors'])[0]
    
    for i in range(len(id)):
        title.append(list(df[df['id'] == id[i]]['title'])[0])
    
    for i in range(len(title)):
        poster_path.append(poster(id[i]))
    return title,poster_path

def recommend_overview(movie):
    
    title = []
    poster_path = []

    id = list(df[df['title'] == movie]['Recommended_overview'])[0]
    
    for i in range(len(id)):
        title.append(list(df[df['id'] == id[i]]['title'])[0])
    
    for i in range(len(title)):
        poster_path.append(poster(id[i]))
    return title,poster_path

# ----------------------------------------------------------------------------------------------------------
# -----------------------------------Build Streamlit App------------------------------------------
st.title('Movie Recommender')

inp1 = st.selectbox('Select Movie', list(df['title']))
inp2 = st.selectbox('Recommend On Basis of', ['Genres','Actors','Story'])

if st.button('Recommend'):


    if inp2 == 'Genres':
        title,poster_path = recommend_genres(inp1)
        col1, col2,col3,col4,col5 = st.columns(5)
        
        with col1:
            st.markdown(title[0])
            st.image(poster_path[0])
        with col2:
            st.markdown(title[1])
            st.image(poster_path[1])
        with col3:
            st.markdown(title[2])
            st.image(poster_path[2])
        with col4:
            st.markdown(title[3])
            st.image(poster_path[3])
        with col5:
            st.markdown(title[4])
            st.image(poster_path[4])


    elif inp2 == 'Actors':
        title,poster_path = recommend_actors(inp1)
        col1, col2,col3,col4,col5 = st.columns(5)
        
        with col1:
            st.markdown(title[0])
            st.image(poster_path[0])
        with col2:
            st.markdown(title[1])
            st.image(poster_path[1])
        with col3:
            st.markdown(title[2])
            st.image(poster_path[2])
        with col4:
            st.markdown(title[3])
            st.image(poster_path[3])
        with col5:
            st.markdown(title[4])
            st.image(poster_path[4])
    
    elif inp2 == 'Story':
        title,poster_path = recommend_overview(inp1)
        col1, col2,col3,col4,col5 = st.columns(5)
        
        with col1:
            st.markdown(title[0])
            st.image(poster_path[0])
        with col2:
            st.markdown(title[1])
            st.image(poster_path[1])
        with col3:
            st.markdown(title[2])
            st.image(poster_path[2])
        with col4:
            st.markdown(title[3])
            st.image(poster_path[3])
        with col5:
            st.markdown(title[4])
            st.image(poster_path[4])

    
    

