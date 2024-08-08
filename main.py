import pygwalker as pyg
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

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
    encoding_options = ['latin1', 'utf-8', 'ISO-8859-1', 'cp1252']
    df = None
    
    for encoding in encoding_options:
        try:
            df = pd.read_csv(uploaded_file, encoding=encoding)
            st.success(f"File successfully loaded with encoding: {encoding}")
            break
        except UnicodeDecodeError:
            st.warning(f"Failed to decode with encoding: {encoding}. Trying next encoding...")
    
    if df is not None:
        # Generate the HTML of the PyGWalker object
        pyg_html = pyg.walk(df, return_html=True)

        # Embed the HTML into the Streamlit app
        components.html(pyg_html, height=1000, scrolling=True)
    else:
        st.error("Unable to decode the file with the provided encodings. Please upload a valid CSV file.")
else:
    st.warning("Please upload a CSV file to proceed.")
