"""
this module is designed to take the shift_setup.csv and the availability.csv
and generate a list of lists that will be used in roster_model.py as the 
data structure that is passed through the optimistaion algorithm

"""

import pandas as pd

available = pd.read_csv("data/availability.csv")
shifts = pd.read_csv("data/shift_setup.csv")

print(shifts.head())