import streamlit as st

with st.sidebar:
    st.logo("Data/logo.svg", link="https://www.themoviedb.org/")

    st.write("A simple film recommender using vector mathematics. Click on Information to find out more")

    st.write("Created by Thomas Collins 2024. Poster images loaded from themoviedatabase.org")

pages = st.navigation([st.Page("home.py", title="Home"), st.Page("infoPage.py", title="Information")])
pages.run()
