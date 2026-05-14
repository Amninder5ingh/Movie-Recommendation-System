import streamlit as st
import pickle

movies = pickle.load(open("movie.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(film):
    index = movies[movies['title'] == film].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recom = []
    for i in distances[1:6]:
        recom.append(movies.iloc[i[0]].title)
    return recom
st.title("Movie Recommendation System")

selected = st.selectbox(
    "Select Movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendation = recommend(selected)
    for i in recommendation:
        st.write(i)