from re import M
from numpy import append
import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie


st.title('Movie Recommender System')

movie_dict = pickle.load(open('movie_data.pkl', 'rb'))
#movie_list = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie = st.selectbox(
 'Watch Now',
movie_dict['title'].values)

def fetch_posters(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=42ee447924e1c50edacf362f03880bd6'.format(movie_id))
    data =response.json()
    path ="https://image.tmdb.org/t/p/w500"+ data['poster_path']
    return path


def recommend(movie):
    x = movie_dict[movie_dict['title'] == movie].index[0]
    distance = similarity[x]
    mov_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommmended_movies = []
    recommended_poster = []

    for i in mov_list:
        id = movie_dict.iloc[i[0]].movie_id
        recommmended_movies.append(movie_dict.iloc[i[0]].title)
        recommended_poster.append(fetch_posters(id))
    return recommmended_movies ,recommended_poster
    
if st.button('Recommend'):
    names, poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(names[0])
        st.image(poster[0])

    with col2:
        st.write(names[1])
        st.image(poster[1])

    with col3:
        st.write(names[2])
        st.image(poster[2])

    with col4:
        st.write(names[3])
        st.image(poster[3])

    with col5:
        st.write(names[4])
        st.image(poster[4])
    