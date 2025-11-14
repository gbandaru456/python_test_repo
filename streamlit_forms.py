import pandas as pd
import streamlit as st

Retaier_df=pd.DataFrame({
    "Retaier_id": [1,11,14,15,16,17,29,30,31,32,33,53,62,72],
    "Retaier_name": ['Amazon.com','Amazon Canada','Amazon Germany','Amazon France','Amazon Japan','Amazon UK','Amazon Italy','Amazon Spain','Amazon Australia','Amazon Mexico','Amazon Brazil','Amazon UAE','Amazon Netherlands','Amazon KSA'],
    "Country_code": ['US','CA','DE','FR','JP','GB','IT','ES','AU','MX','BR','AE','NL','SA'],
    "Brand":['Mevo','JayBird','Blue','BlueMic','Logitech G','Astro','Logicool','Logitech','Ultimate Ears','test','test','test','test','test'],
    "Category":['Keyboard & Mice','Gaming Accessories','Portable Audio & Speakers','Headphones','TV Mounts & Stands','Computer Cables & Interconnects','Keychains, Keyrings & Carabiners','Watches & Accessories','Desktops','Motorcycle Parts','Electronics Mounts & Stands','Automotive Suspension','Tablets','Memory Cards & Flash Drives'],
    "Sub_category":['Computer Webcams & Accessories','Multipurpose Condenser Microphones','Gaming Keyboards','Gaming Accessory Bundles & Combos','Other Keyboard & Mouse Accessories',
    'Camera Accessory Bundles','USB-to-USB Adapters','Tablet Stands','Camcorders','MP3 & MP4 Player Accessories','Water Flavoring Drops','Other Camera Accessories & Equipment',
    'Home Audio Stereo Jack Cables','Home Security Systems']
})
st.write("Stackline_beacon sales entry from")
with st.form("form_key"):
     
     RETAILER_ID=st.selectbox(label="Retaier_id",placeholder="Choose an option",options=Retaier_df["Retaier_id"].to_list())
     RETAILER_NAME=st.selectbox("Retaier_name",placeholder="Choose an option",options=Retaier_df["Retaier_name"].to_list())
     COUNTRY_CODE=st.selectbox("Country_code",placeholder="Choose an option",options=Retaier_df["Country_code"].to_list())
     RETAILER_SKU=st.text_input(label="Retailer_sku",placeholder="Retailer_sku")
     UPC=st.text_input(label="UPC",placeholder="UPC")
     MODEL_NUMBER=st.text_input(label="Model_number",placeholder="Model_number")
     TITLE=st.text_input(label="Title",placeholder="Title",key="title_1")
     BRAND=st.selectbox("Brand",placeholder="Choose an option",options=Retaier_df["Brand"].to_list())
     CATEGORY=st.selectbox("Category",placeholder="Choose an option",options=Retaier_df["Category"].to_list())
     SUBCATEGORY=st.selectbox("Sub_category",placeholder="Choose an option",options=Retaier_df["Sub_category"].to_list())
     AVAILABILITY_STATUS=st.radio("status",options=["Active","Inactive"],horizontal=True,index=0)
     AVAILABILITY_STATUS_CODE=st.radio("status_code",options=["Temporarily unavailable","In stock","Permanently unavailable"],horizontal=True,index=0)
     WEEK_ID=st.text_input(label="Week_id",placeholder="Week_id",max_chars=6)
     WEEK_BEGINNING=st.date_input(label="Week_begining",value='today')
     WEEK_ENDING=st.date_input(label="Week_ending",value='today')
     UNITS_SOLD=st.number_input(label="Unit_sold",placeholder="Unit_sold")
     RETAIL_PRICE=st.number_input(label="Retailer_proce",placeholder="Retailer_proce")
     RETAIL_SALES=st.number_input(label="Retail_sales",placeholder="Retail_sales")
     submit_btn=st.form_submit_button("Submit")
     st.write(f""" your product details are:
              RETAILER_ID : {RETAILER_ID}
              RETAILER_NAME : {RETAILER_NAME}
              COUNTRY_CODE : {COUNTRY_CODE}
              RETAILER_SKU : {RETAILER_SKU}
              UPC : {UPC}
              MODEL_NUMBER : {MODEL_NUMBER}
              TITLE : {TITLE}
              BRAND : {BRAND}
              CATEGORY : {CATEGORY}
              SUBCATEGORY : {SUBCATEGORY}
              AVAILABILITY_STATUS : {AVAILABILITY_STATUS}
              AVAILABILITY_STATUS_CODE : {AVAILABILITY_STATUS_CODE}
              WEEK_ID : {WEEK_ID}
              WEEK_BEGINNING : {WEEK_BEGINNING}
              WEEK_ENDING : {WEEK_ENDING}
              """)
