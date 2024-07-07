import pickle
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

st.title("MOVIE RECOMMENDATIONS FOR YOU !!")

# Load the data
with open("movies.pkl", "rb") as file1:
    new_df = pickle.load(file1)

with open("similarity_matrix.pkl", "rb") as file2:
    similarity_matrix = pickle.load(file2)

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_matrix[movie_index])), reverse=True, key=lambda x: x[1])
    recommendations = [new_df.iloc[i[0]].title for i in distances[1:6]]
    return recommendations

# Generate movie list for selection
movie_list = new_df['title'].values

# User selects a movie
selected_movie = st.selectbox(label="Please choose a movie from the dropdown list to get similar recommendations.", options=movie_list)

# Recommend movies when the button is clicked
if st.button(label="RECOMMEND"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.success('Your movie recommendations are ready! Enjoy your next watch!', icon="✅")
    # st.write("Recommended movies:")
    for movie in recommendations:
        st.write(movie)


st.write(selected_movie)
