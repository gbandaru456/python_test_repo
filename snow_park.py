import pandas as pd
import streamlit as st

#Header
st.title("This is my first APP")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})

edited_df = st.data_editor(df, num_rows="dynamic")

df1 = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]    
)
edited_df = st.data_editor(df1, num_rows="dynamic")
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
#buttons
update=st.button(label="update",type="primary")
if update:
    st.write("you have choose upadte")
delete=st.button(label="delete",type="primary")
if delete:
    st.write("you have select delete")
read=st.button(label="read",type="primary")
if read:
    st.write("you have seleced on read")
create=st.button(label="create",type="primary")
if create:
    st.write("you have choosen create")

#checkbox
st.divider()
male=st.checkbox("male")
if male:
    st.write("Male")
female=st.checkbox("Female")
if female:
    st.write("Female")
transnder=st.checkbox("transender",disabled=True)
if transnder:
    st.write("Trans")
#Radio button



radio=st.radio("choose person",options=df.columns[1:],index=0,horizontal=True)
st.write(radio)
st.divider()
select=st.selectbox("choose person",options=df.columns[1:],index=0)
st.write(select)

name=st.text_input("write your name",placeholder="Govardhan")
st.write(f"your name is {name}")