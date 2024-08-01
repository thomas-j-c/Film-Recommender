import streamlit as st
import pickle
import requests

def getPoster(filmID):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=1c35f49765d39585e570f35036513c0a&language=en-US".format(filmID)
    data = requests.get(url).json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def findRecommendation(input):
    filmIndex = films[films["title"] == input].index[0]
    distance = sorted(list(enumerate(simMatrix[filmIndex])),
                      reverse=True, key=lambda vector: vector[1])

    recommendations = []
    posters = []
    for i in distance[1: 6]:
        recommendations.append(films.iloc[i[0]].title)

        posters.append(getPoster(films.iloc[i[0]].id))

    return recommendations, posters


films = pickle.load(open("Data/films.pkl", "rb"))
filmTitles = films["title"].values

simMatrix = pickle.load(open("Data/similarity_matrix.pkl", "rb"))

st.header("Film Recommender")
selectValue = st.selectbox("Select a film", filmTitles)

columns = st.columns(5)
names, posters = findRecommendation(selectValue)
for index, column in enumerate(columns):
    with column:
        st.text(names[index])
        st.image(posters[index], use_column_width=True)
