import requests
import streamlit as st
import pickle
import pandas as pd

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
#         movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path


def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distance = similar[movie_idx]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies




movies_dic = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dic)
similar = pickle.load(open('similar.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would u like to be contacted',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
