import streamlit as st
import pandas as pd

st.session_state.availability_df = pd.read_csv('data/availability.csv')
st.session_state.availability_df.reset_index(drop=True, inplace=True)

# bring in the employees data as we need the 'Name' column to use as an index in the shift_df dataframe
st.session_state.employees_df = pd.read_csv('data/employees.csv')
st.session_state.employees_df.reset_index(drop=True, inplace=True)

names = st.session_state.employees_df['Name'].values.tolist()

st.title("Leave Requests")
st.write("The purpose of this page is to allow admin/ supervisor to be able \
    to update leave requests and save the updates to the csv file")

st.subheader("Current Leave Requests")
if st.checkbox("Show Leave Requests"):
    st.subheader("Leave Requests")
    st.table(st.session_state.availability_df)


# this needs to be a list from the employees csv file
emp_list = st.selectbox("Employee Name",names)

date = st.date_input("Select Date")

#shift = st.radio("Please select your shift",
#('Day','Night'))


st.subheader('Edit the employees dataframe')

if st.button('Update'):
    new_entry = [{'Employee':emp_list, 'Date':date}]
    st.session_state.availability_df = st.session_state.availability_df.append(new_entry)
    st.session_state.availability_df.to_csv('data/availability.csv',index=False)
