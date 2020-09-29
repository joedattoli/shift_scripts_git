# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:39:05 2020

@author: joedattoli
"""

import os
import pandas as pd 
import glob
import runpy
import numpy 
    
def get_zone_metric(dataframe,metric1,metric2,qual):
    zone_series = dataframe['zone'].unique()
    zone_series = list(zone_series)
    zone_series.append(0)
    zone_series_app=[]
    metric1_series =[]
    metric2_series =[]
    qual1 = metric1 + '_' + qual
    qual2 = metric2 + '_' + qual
    for zone in zone_series:
        if zone == 0:
            temp_frame = dataframe
            metric1_series.append(temp_frame[metric1].mean())
            metric2_series.append(temp_frame[metric2].mean())
            zone_series_app.append(zone)
        else:
            temp_frame = dataframe.loc[dataframe['zone']==zone]
            metric1_series.append(temp_frame[metric1].mean())
            metric2_series.append(temp_frame[metric2].mean())
            zone_series_app.append(zone)
        
    malu_frame = pd.DataFrame({'zone': zone_series_app, qual1 : metric1_series, qual2 : metric2_series })
    
    return malu_frame
    
## get and put together the csv's of batted balls    
os.chdir(r"C:\Users\joedattoli\Desktop\ShiftScripts")
'''
#outdated piece of code. Circumvented the need for glober but want to keep this here for reference purposes
glober = glob.glob(os.getcwd()+"/*.csv")

dataframes = []
for globy in glober:
    dataframes.append(pd.read_csv(globy))
batted_balls = pd.concat(dataframes, ignore_index = True)
'''

os.chdir(r"C:\Users\joedattoli\Desktop\ShiftScripts")

batted_balls = pd.read_excel(r"raw_batted_balls.xlsx")


batted_balls_L = batted_balls.loc[batted_balls['stand']== 'L']
batted_balls_R = batted_balls.loc[batted_balls['stand']== 'R']

batted_balls_stand = batted_balls.loc[batted_balls['if_fielding_alignment']== 'Standard']
batted_balls_strat = batted_balls.loc[batted_balls['if_fielding_alignment']== 'Strategic']
batted_balls_shift = batted_balls.loc[batted_balls['if_fielding_alignment']== 'Infield shift']

batted_balls_stand_L = batted_balls_L.loc[batted_balls_L['if_fielding_alignment']== 'Standard']
batted_balls_strat_L = batted_balls_L.loc[batted_balls_L['if_fielding_alignment']== 'Strategic']
batted_balls_shift_L = batted_balls_L.loc[batted_balls_L['if_fielding_alignment']== 'Infield shift']

batted_balls_stand_R = batted_balls_R.loc[batted_balls_R['if_fielding_alignment']== 'Standard']
batted_balls_strat_R = batted_balls_R.loc[batted_balls_R['if_fielding_alignment']== 'Strategic']
batted_balls_shift_R = batted_balls_R.loc[batted_balls_R['if_fielding_alignment']== 'Infield shift']

batted_balls_frame = get_zone_metric(batted_balls,'woba_value','estimated_woba_using_speedangle', 'all')

batted_balls_L_frame = get_zone_metric(batted_balls_L,'woba_value','estimated_woba_using_speedangle', 'L')
batted_balls_R_frame = get_zone_metric(batted_balls_R,'woba_value','estimated_woba_using_speedangle', 'R')

batted_balls_stand_frame = get_zone_metric(batted_balls_stand,'woba_value','estimated_woba_using_speedangle', 'standard')
batted_balls_strat_frame = get_zone_metric(batted_balls_strat,'woba_value','estimated_woba_using_speedangle', 'strategic')
batted_balls_shift_frame =get_zone_metric(batted_balls_shift,'woba_value','estimated_woba_using_speedangle', 'shift')

batted_balls_stand_L_frame = get_zone_metric(batted_balls_stand_L,'woba_value','estimated_woba_using_speedangle', 'standard_L')
batted_balls_strat_L_frame = get_zone_metric(batted_balls_strat_L,'woba_value','estimated_woba_using_speedangle', 'strategic_L')
batted_balls_shift_L_frame = get_zone_metric(batted_balls_shift_L,'woba_value','estimated_woba_using_speedangle', 'shift_L')

batted_balls_stand_R_frame = get_zone_metric(batted_balls_stand_R,'woba_value','estimated_woba_using_speedangle', 'standard_R')
batted_balls_strat_R_frame = get_zone_metric(batted_balls_strat_R,'woba_value','estimated_woba_using_speedangle', 'strategic_R')
batted_balls_shift_R_frame = get_zone_metric(batted_balls_shift_R,'woba_value','estimated_woba_using_speedangle', 'shift_R')


big_frame = batted_balls_frame
big_frame = big_frame.sort_values('zone').reset_index(drop = True)


big_list = [batted_balls_L_frame,batted_balls_R_frame,
            batted_balls_stand_frame,batted_balls_strat_frame,batted_balls_shift_frame,
            batted_balls_stand_L_frame,batted_balls_strat_L_frame,batted_balls_shift_L_frame,
            batted_balls_stand_R_frame,batted_balls_strat_R_frame,batted_balls_shift_R_frame]
for big in big_list:
    big.sort_values('zone').sort_values('zone').reset_index(drop = True)
    big_frame = big_frame.merge(big,left_on ='zone', right_on ='zone')
    
    
with pd.ExcelWriter(r"C:\Users\joedattoli\Desktop\ShiftScripts\zoned_batted_balls.xlsx") as writer:
    big_frame.to_excel(writer)