from re import M
from numpy import append
import streamlit as st
import pickle
import pandas as pd
import requests

st.title('Movie Recommender')

movie_dict = pickle.load(open('movie_data_dict.pkl', 'rb'))
movie_list = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie = st.selectbox(
 'How would you like to be contacted?',
movie_list['title'].values)

###def fetch_posters(movie_id):
# response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=42ee447924e1c50edacf362f03880bd6'.format(movie_id))
# data =response.json()
# st.text(data)
# return "https://image.tmdb.org/t/p/w500"+ data['poster_path']


def recommend(movie):
    x = movie_list[movie_list['title'] == movie].index[0]
    distance = similarity[x]
    mov_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommmended_movies = []
    #recommended_poster = []

    for i in mov_list:
        #id = movie_list.iloc[i[0]].movie_id
        recommmended_movies.append(movie_list.iloc[i[0]].title)
        #recommended_poster = fetch_posters(id)
    return recommmended_movies #,recommended_poster
    
if st.button('Recommend'):
    names = recommend(selected_movie)
    for i in names:
        st.write(i)


  