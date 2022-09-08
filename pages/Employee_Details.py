import streamlit as st
import pandas as pd


st.session_state.employees_df = pd.read_csv('data/employees.csv')
st.session_state.employees_df.reset_index(drop=True, inplace=True)

st.title("Employee Details")
st.write("The purpose of this page is to allow admin/ supervisor to be able \
    to remove or add employees and save the updates to the csv file")

st.subheader("Current Employee Data")
if st.checkbox("Show current employees"):
    st.subheader("Current Employees")
    st.table(st.session_state.employees_df)

st.subheader('Edit the employees dataframe')
option = st.selectbox('What action would you like to perform',('Add Employee','Remove Employee'))

name = st.text_input('Enter the employees name')
depot = st.selectbox('Select the depot',('Perth','Bunbury'))

if st.button('Update'):
    if option == 'Add Employee':
        new_entry = [{'Name':name, 'Depot':depot,'Position':'Controller'}]
        st.session_state.employees_df = st.session_state.employees_df.append(new_entry)

    else:
        st.session_state.employees_df.drop(st.session_state.employees_df[st.session_state.employees_df['Name'] == name].index, inplace = True)
    
    
    st.session_state.employees_df.to_csv('data/employees.csv',index=False)


