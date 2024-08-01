import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

films = pd.read_csv("dataset.csv")

print(films.columns)

films = films[["id", "title", "genre", "overview"]]

films["tags"] = films["genre"] + " " + films["overview"]

films.drop(columns=["genre", "overview"], inplace=True)

vectoriser = CountVectorizer(max_features=10000, stop_words="english")
vector = vectoriser.fit_transform(films["tags"].values.astype("U")).toarray()

similarity = cosine_similarity(vector)

pickle.dump(films, open("films.pkl", "wb"))
pickle.dump(similarity, open("similarity_matrix.pkl", "wb"))