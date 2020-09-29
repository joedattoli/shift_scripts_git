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



### SHIFT MEANS
xWOBA_shift_list = batted_balls_shift['estimated_woba_using_speedangle']

xWOBA_shift_mean = xWOBA_shift_list.mean() 

WOBA_shift_list = batted_balls_shift['woba_value']

WOBA_shift_mean = WOBA_shift_list.mean() 

woba_shift_difference = WOBA_shift_mean - xWOBA_shift_mean 


### STRATIGIC MEANS
xWOBA_strategic_list = batted_balls_strategic['estimated_woba_using_speedangle']

xWOBA_strategic_mean = xWOBA_strategic_list.mean() 

WOBA_strategic_list = batted_balls_strategic['woba_value']

WOBA_strategic_mean = WOBA_strategic_list.mean() 

woba_strategic_difference = WOBA_strategic_mean - xWOBA_strategic_mean 


### STANDARD MEANS
xWOBA_standard_list = batted_balls_standard['estimated_woba_using_speedangle']

xWOBA_standard_mean = xWOBA_standard_list.mean() 

WOBA_standard_list = batted_balls_standard['woba_value']

WOBA_standard_mean = WOBA_standard_list.mean() 

woba_standard_difference = WOBA_standard_mean - xWOBA_standard_mean 


### what if we looked at only balls with launch angle between -inf and 10 (any higher LA and INF have to jump to catch it)
batted_balls_la = batted_balls.loc[batted_balls['launch_angle'] <= 10]

batted_balls_shift_la = batted_balls_la.loc[batted_balls['if_fielding_alignment'] == 'Infield shift']
batted_balls_strategic_la = batted_balls_la.loc[batted_balls['if_fielding_alignment'] == 'Strategic']
batted_balls_standard_la = batted_balls_la.loc[batted_balls['if_fielding_alignment'] == 'Standard']


### SHIFT MEANS
xWOBA_shift_list_la = batted_balls_shift_la['estimated_woba_using_speedangle']

xWOBA_shift_mean_la = xWOBA_shift_list_la.mean() 

WOBA_shift_list_la = batted_balls_shift_la['woba_value']

WOBA_shift_mean_la = WOBA_shift_list_la.mean() 

woba_shift_difference_la = WOBA_shift_mean_la - xWOBA_shift_mean_la 


### STRATIGIC MEANS
xWOBA_strategic_list_la = batted_balls_strategic_la['estimated_woba_using_speedangle']

xWOBA_strategic_mean_la = xWOBA_strategic_list_la.mean() 

WOBA_strategic_list_la = batted_balls_strategic_la['woba_value']

WOBA_strategic_mean_la = WOBA_strategic_list_la.mean() 

woba_strategic_difference_la = WOBA_strategic_mean_la - xWOBA_strategic_mean_la 


### STANDARD MEANS
xWOBA_standard_list_la = batted_balls_standard_la['estimated_woba_using_speedangle']

xWOBA_standard_mean_la = xWOBA_standard_list_la.mean() 

WOBA_standard_list_la = batted_balls_standard_la['woba_value']

WOBA_standard_mean_la = WOBA_standard_list_la.mean() 

woba_standard_difference_la = WOBA_standard_mean_la - xWOBA_standard_mean_la



