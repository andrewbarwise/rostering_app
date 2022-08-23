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

st.subheader('Add Employees')


st.subheader("Remove Employees")




