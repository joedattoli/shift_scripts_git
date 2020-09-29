# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:37:39 2020

@author: joedattoli
"""


import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\joedattoli\Desktop\ShiftScripts\baseball_savant.db")

# Query the database and load into a pandas dataframe
#query takes all batted ball events with a registered EV only
df = pd.read_sql_query("SELECT * FROM statcast  WHERE launch_speed >= 0 AND game_year == 2019;", conn)

# Close connection when finished
conn.close()
with pd.ExcelWriter(r"C:\Users\joedattoli\Desktop\ShiftScripts\raw_batted_balls.xlsx") as writer:
    df.to_excel(writer)