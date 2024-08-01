import streamlit as st

st.header("Information about the site")
st.write("The recommendation service is powered using vector mathematics. \n"
         "We use the scikit Learn Countvectorizer class to extract relevant features \n"
         "from a dataset of films, which are the genre and description. \n "
         "\n"
         "These features are then learnt, and the document-term matrix is returned \n"
         "using the fit_transform method. The cosine similarity of the matrix was \n"
         "found to find a model where similar films had a smaller number and less similar \n"
         "ones had a larger number.")

st.write("A code snippet can be seen:")


code = """
vectoriser = CountVectorizer(max_features=10000, stop_words='english')
vector = vectoriser.fit_transform(films['tags'].values.astype('U')).toarray()

similarity = cosine_similarity(vector)
"""

st.code(code)


