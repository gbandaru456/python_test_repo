# Import python packages
import streamlit as st
import pandas as pd

st.title("csv file upload")
menu=["Home","Dataset"]
choose=st.sidebar.selectbox("menu",menu)
if choose=="Home":
    st.subheader("Home")
else:
    st.subheader("Dataset")
    data_file=st.file_uploader("upload_csv",type=["csv"])
    if data_file is not None:
           file_datails={"filename":data_file.name,"file_type":data_file.type,"file_size":data_file.size}
           df=pd.read_csv(data_file)
           st.write(file_datails)           
           df["file_name"]=data_file.name
           st.dataframe(df[0])

