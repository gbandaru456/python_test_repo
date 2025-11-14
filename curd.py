import psycopg2
import pandas as pd
import streamlit as st

conn = psycopg2.connect(database='Cars_DB',user='postgres', password='postgres', host='localhost', port='5432')
cursor = conn.cursor()
print("Connection established")
#create steamlit
st.balloons()
st.title("CURD operation")
option=st.sidebar.selectbox("select an operation",("Create","Read","Update","Delete"))
st.image('./source/logi.jpg',use_column_width=True)
if option=="Create":
    st.subheader("Create a record")
    Retailer_id=st.text_input("enter Retailer_id", max_chars=3)
    Retailer_name=st.text_input("enter Retailer_name")
    Retailer_sku=st.text_input("enter Retailer_sku")
    Week_id=st.text_input("enter week_id")
    if st.button("Create"):
        sql="insert into stack_line_inhouse_share (retailer_id,retailer_name,retailer_sku,week_id) values (%s,%s,%s,%s)"
        val=(Retailer_id,Retailer_name,Retailer_sku,Week_id)
        cursor.execute(sql,val)
        conn.commit()
        st.success("Record created successful !!!")
        conn.close()
elif option=="Read":
        st.subheader("Read records")
        ids = st.text_input('Enter Retailer_ID')
        if st.button("Fetch"):
         sql1="select * from stack_line_inhouse_share where retailer_id=%s"
         val4=(ids,)
         cursor.execute(sql1,val4)
         result=cursor.fetchall()
         for row in result:
            st.write(row)
            conn.close()
elif option=="Update":
     st.subheader("Update Record")
     ret_id=st.text_input("enter retailer_id")
     ret_name=st.text_input("enter new retailer_name")
     ret_sku=st.text_input("enter retailer_sku")
     weekid=st.text_input("enter week_id")
     if st.button("Update"):
          sql3="update stack_line_inhouse_share set retailer_name=%s,retailer_sku=%s,week_id=%s where retailer_id=%s"
          val3=(ret_name,ret_sku,weekid,ret_id)
          cursor.execute(sql3,val3)
          conn.commit()
          st.success("Record updated scuccsfull !!")
          conn.close()

elif option=="Delete":
     st.subheader("Delete a record")
     id=st.text_input("enter Retailer_id")
     if st.button("Delete"):
          sql2="delete from stack_line_inhouse_share where retailer_id =%s"
          val1=(id,)
          cursor.execute(sql2,val1)
          conn.commit()
          st.success("Record Deleted")
          conn.close()




