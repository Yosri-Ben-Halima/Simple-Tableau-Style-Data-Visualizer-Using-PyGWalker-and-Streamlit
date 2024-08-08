import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Adjust the width and title of the Streamlit page
st.set_page_config(
    page_title="Pygwalker Data Visualization App Using Streamlit",
    layout="wide"
)

st.title("Pygwalker Data Visualization App Using Streamlit")

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Attempt to load the data into a DataFrame with various encodings
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(uploaded_file, encoding='cp1252')
            except UnicodeDecodeError:
                st.error("Failed to decode the file. Please check the file encoding.")
                df = None

    if df is not None:
        # Generate the HTML of the PyGWalker object
        pyg_html = pyg.walk(df, return_html=True)

        # Embed the HTML into the Streamlit app
        components.html(pyg_html, height=1000, scrolling=True)
    else:
        st.warning("Unable to load the CSV file. Please upload a valid file.")
else:
    st.warning("Please upload a CSV file to proceed.")
