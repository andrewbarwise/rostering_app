from datetime import datetime
import streamlit as st
import pandas as pd
from datetime import timedelta

# bring in the employees data as we need the 'Name' column to use as an index in the shift_df dataframe
st.session_state.employees_df = pd.read_csv('data/employees.csv')
st.session_state.employees_df.reset_index(drop=True, inplace=True)

names = st.session_state.employees_df['Name'].values.tolist()

st.title("Shift Setup Details")
st.write("The purpose of this page is to allow admin/ supervisor to be able \
    to remove or add employees and save the updates to the csv file")

min_date = datetime.date(datetime.now())
max_date =  min_date + timedelta(days=365)
date_range = st.date_input("Select the date range",(min_date, max_date))

days = pd.date_range(date_range[0], date_range[1], freq='d').to_list()

st.session_state.shift_df = pd.DataFrame(columns=days,index=names)
st.session_state.shift_df.iloc[:] = 1

st.subheader("Current shift setup data")
if st.checkbox("Show shift setup data"):
    st.subheader("Shifts")
    st.table(st.session_state.shift_df)

# save the shift_df as a csv file into the data folder
st.session_state.shift_df.to_csv("data\shift_setup.csv")

