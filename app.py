# import streamlit as st
# import pickle
# import pandas as pd

# def recommend(movie):

# # movie_index = new_df[new_df['title'] == movie].index[0]
# #   distances = similarity[movie_index]
# #   movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

# #   for i in movies_list:
# #     print(new_df.iloc[i[0]].title)  

#   movie_index = movies_list[movies_list['title'] == movie].index[0]
#   distances = similarity[movie_index]
#   movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  
#   recommended_movies = []
#   for i in movies:
#     recommended_movies.append(movies_list.iloc[i[0]].title)
#   return recommended_movies

# movies_list = pickle.load(open('movies.pkl','rb'))
# movies_list = movies_list['title'].values

# similarity = pickle.load(open('similarity.pkl','rb'))

# st.title('Movie Recommender System')

# selected_movie_name = st.selectbox('Search for Movies',movies_list)

# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=82215dbc84c428f934d24a86ccd1b022&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    # Get the index of the selected movie
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    # Sort by similarity and get the top 5 recommendations
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies:
        movie_id = new_df.iloc[i[0]].movie_id  # Access the DataFrame instead of movies_list
        recommended_movies.append(new_df.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_movies_posters

# Load movie list and similarity matrix
new_df = pickle.load(open('movies.pkl', 'rb'))  # Assuming this is a DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit App UI
st.title('Movie Recommender System')

movies_list = new_df['title'].values
selected_movie_name = st.selectbox('Search for Movies', movies_list)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
