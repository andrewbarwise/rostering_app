import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def get_data():
    return []


emp_list = st.selectbox("Employee Name",
('James','Molly','Sam','Melissa'))

date = st.date_input("Select Date")

shift = st.radio("Please select your shift",
('Day','Night'))

if st.button('Update'):
    get_data().append({'Employee':emp_list,'Date':date,'Shift':shift})

st.write(pd.DataFrame(get_data()))