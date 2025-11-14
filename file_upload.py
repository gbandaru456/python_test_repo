import streamlit as st
import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.dataframe(bytes_data)
