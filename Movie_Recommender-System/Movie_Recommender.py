import streamlit as st
import pickle
import pandas as pd
import requests
import os

# Setting the TMDb API key as an environment variable
os.environ['TMDB_API_KEY'] = 'e7066c35775d6ec6662d8b41d2c86f1d'

st.title("MOVIES RECOMMENDER SYSTEM")

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie = st.selectbox("Type or select a movie from the dropdown", movies['title'].values)

def recommend(movie):
    movieIndex = movies[movies['title'] == movie].index[0]
    dist = similarity[movieIndex]
    moviesList = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in moviesList:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

def fetch_poster(movie_id):
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')

    if TMDB_API_KEY is None:
        st.error("Please set your TMDb API key as an environment variable.")
        return None

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    data = requests.get(url)

    if data.status_code != 200:
        st.error("Failed to fetch data from TMDb API.")
        return None

    data = data.json()
    poster_path = data.get('poster_path')

    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        st.warning("Poster not found for this movie.")
        return None

if st.button('SHOW RECOMMENDATIONS'):
    names, posters = recommend(selected_movie)

    # Create columns for displaying recommendations and posters
    cols = st.columns(5)

    for i, col in enumerate(cols):
        if i < len(names):
            col.text(names[i])
            if posters[i]:
                col.image(posters[i])
