# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:42:09 2020

@author: joedattoli
"""

import os
import pandas as pd 
import glob
import seaborn as sb
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\joedattoli\Desktop\StatCastCSV")
glober = glob.glob(os.getcwd()+"/*.csv")

dataframes = []
for globy in glober:
    dataframes.append(pd.read_csv(globy))
    
batted_balls = pd.concat(dataframes, ignore_index = True)

batted_balls_shift = batted_balls.loc[batted_balls['if_fielding_alignment'] == 'Infield shift']
batted_balls_strategic = batted_balls.loc[batted_balls['if_fielding_alignment'] == 'Strategic']
batted_balls_standard = batted_balls.loc[batted_balls['if_fielding_alignment'] == 'Standard']


## Plot Exit Velo and Launch Angles
batted_balls_shift_ev = batted_balls_shift['launch_speed']
batted_balls_standard_ev = batted_balls_standard['launch_speed']
batted_balls_strategic_ev = batted_balls_strategic['launch_speed']

sb.distplot(batted_balls_shift_ev,bins=20, label = 'shift')
sb.distplot(batted_balls_standard_ev, bins=20, label = 'standard' )
sb.distplot(batted_balls_strategic_ev, bins=20, label = 'strat')
plt.legend()
plt.show()

