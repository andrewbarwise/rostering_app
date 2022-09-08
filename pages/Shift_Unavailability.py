import streamlit as st
import pandas as pd

st.session_state.availability_df = pd.read_csv('data/availability.csv')
st.session_state.availability_df.reset_index(drop=True, inplace=True)

st.title("Employee Details")
st.write("The purpose of this page is to allow admin/ supervisor to be able \
    to update leave requests and save the updates to the csv file")

st.subheader("Current Leave Requests")
if st.checkbox("Show Leave Requests"):
    st.subheader("Leave Requests")
    st.table(st.session_state.availability_df)


# this needs to be a list from the employees csv file
emp_list = st.selectbox("Employee Name",('James','Molly','Sam','Melissa'))

date = st.date_input("Select Date")

shift = st.radio("Please select your shift",
('Day','Night'))


st.subheader('Edit the employees dataframe')

if st.button('Update'):
    new_entry = [{'Employee':emp_list, 'Date':date,'Shift':shift}]
    st.session_state.availability_df = st.session_state.availability_df.append(new_entry)
    st.session_state.availability_df.to_csv('data/availability.csv',index=False)
