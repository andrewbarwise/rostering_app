from datetime import datetime
import streamlit as st
import pandas as pd
from datetime import timedelta

min_date = datetime.date(datetime.now())
max_date =  min_date + timedelta(days=365)
date_range = st.date_input("Select the date range",(min_date, max_date))

days = pd.date_range(date_range[0], date_range[1], freq='d').to_list()

st.write(days)