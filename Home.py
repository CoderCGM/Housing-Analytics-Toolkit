import streamlit as st
from PIL import Image

st.set_page_config(layout="centered",initial_sidebar_state="auto")
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="👋",
)
st.markdown('''
# :orange[Welcome Aboard]  
## :blue[Are you ready to choose your new Home?]  
''')
image = Image.open('images/Real Estate Recommender.png')
st.image(image)


