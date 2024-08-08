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
    encoding_options = ['utf-8', 'latin1', 'ISO-8859-1', 'cp1252']
    df = None
    
    for encoding in encoding_options:
        try:
            df = pd.read_csv(uploaded_file, encoding=encoding)
            st.success(f"File successfully loaded with encoding: {encoding}")
            break
        except UnicodeDecodeError:
            st.warning(f"Failed to decode with encoding: {encoding}. Trying next encoding...")
            
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    })
    
    if df is not None:
        try:
            # Generate the HTML of the PyGWalker object
            pyg_html = pyg.walk(df, return_html=True)
            
            # Ensure pyg_html is a string
            if isinstance(pyg_html, str):
                # Embed the HTML into the Streamlit app
                components.html(pyg_html, height=1000, scrolling=True)
            else:
                st.error("The generated HTML is not a valid string. Please check the PyGWalker output.")
        except Exception as e:
            st.error(f"An error occurred while generating or displaying the PyGWalker visualization: {e}")
    else:
        st.error("Unable to decode the file with the provided encodings. Please upload a valid CSV file.")
else:
    st.warning("Please upload a CSV file to proceed.")
