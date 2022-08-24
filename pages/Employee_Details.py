import streamlit as st
import pandas as pd

employees_df = pd.read_csv('data\employees.csv')

st.title("Employee Details")
st.write("The purpose of this page is to allow admin/ supervisor to be able \
    to remove or add employees and save the updates to the csv file")

st.subheader("Current Employee Data")
if st.checkbox("Show current employees"):
    st.subheader("Current Employees")
    st.table(employees_df)

st.subheader('Edit the employees dataframe')
option = st.selectbox('What action would you like to perform',('Add Employee','Remove Employee'))

name = st.text_input('Enter the employees name')
depot = st.selectbox('Select the depot',('Perth','Bunbury'))

if st.button('Update'):
    employees_df.concat({'Name':name,'Depot':depot,'Position':'Controller'}, ignore_index=True)
    employees_df.to_csv('data/employees.csv')


