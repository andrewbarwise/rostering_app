import streamlit as st
import pandas as pd

st.title("Rostering Program")

#new_emp = st.text_input('Please enter the employee name')

emp_list = st.selectbox("Employee Name",
('James','Molly','Sam','Melissa'))

date = st.date_input("Select Date")

shift = st.radio("Please select your shift",
('Day','Night'))

df = pd.DataFrame(columns=['Date','Employee','Shift'])

st.dataframe(df)