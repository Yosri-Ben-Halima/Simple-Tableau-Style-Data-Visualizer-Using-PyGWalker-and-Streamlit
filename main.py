import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Load the data
df = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\kaggle_income.csv", encoding='latin1')

# Adjust the width and title of the Streamlit page
st.set_page_config(
    page_title="Pygwalker Data Visualization App Using Streamlit",
    layout="wide"
)

st.title("Pygwalker Data Visualization App Using Streamlit")

# Generate the HTML of the PyGWalker object
pyg_html = pyg.walk(df, return_html=True)

# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
