# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:39:05 2020

@author: joedattoli
"""

import os
import pandas as pd 
import glob
import multiprocessing
import numpy as np
import runpy

## gets the average wOBA for each player in frame vs all infield alignments, just standard,
## vs strategic alignments, or shifted: position = -1,0,1,2 respectively. exp == True will obtain the xwOBA at those positions
## gets the average wOBA for each player in frame vs all infield alignments, just standard,
## vs strategic alignments, or shifted: position = -1,0,1,2 respectively. exp == True will obtain the xwOBA at those positions
def get_player_mean_woba(player_id,dataframe,exp = False, position=-1):
    if (position == 0):
        dataframe = dataframe.loc[dataframe['if_fielding_alignment'] == 'Standard']
        if (exp == False):
            player_woba_list = dataframe.loc[dataframe['batter'] == player_id]
            mean  = player_woba_list['woba_value'].mean()
            return mean
        else:
            player_woba_list = dataframe.loc[dataframe['batter'] == player_id]
            mean  = player_woba_list['estimated_woba_using_speedangle'].mean()
            return mean
    
    elif (position == 1):
        dataframe = dataframe.loc[dataframe['if_fielding_alignment'] == 'Strategic']
        if (exp == False):
            player_woba_list = dataframe.loc[dataframe['batter'] == player_id]
            mean  = player_woba_list['woba_value'].mean()
            return mean
        else:
            player_woba_list = dataframe.loc[dataframe['batter'] == player_id]
            mean  = player_woba_list['estimated_woba_using_speedangle'].mean()
            return mean
    
    elif (position == 2):
        dataframe = dataframe.loc[dataframe['if_fielding_alignment'] == 'Infield shift']
        if (exp == False):
            player_woba_list = dataframe.loc[dataframe['batter'] == player_id]
            mean  = player_woba_list['woba_value'].mean()
            return mean
        else:
            player_woba_list = dataframe.loc[dataframe['batter'] == player_id]
            mean  = player_woba_list['estimated_woba_using_speedangle'].mean()
            return mean
    else:
        if (exp == False):
            player_woba_list = dataframe.loc[dataframe['batter'] == player_id]
            mean  = player_woba_list['woba_value'].mean()
            return mean
        else:
            player_woba_list = dataframe.loc[dataframe['batter'] == player_id]
            mean  = player_woba_list['estimated_woba_using_speedangle'].mean()
            return mean
        
## gets the average exit velocity for each player in frame at the same positions as above
def get_player_mean_ev(player_id,dataframe, position = -1):
    if (position == 0):
        player_frame = dataframe.loc[dataframe['batter'] == player_id]
        df1= player_frame.loc[player_frame['if_fielding_alignment'] == 'Standard']
        mean = df1['launch_speed'].mean()
    
    elif (position == 1):
        player_frame = dataframe.loc[dataframe['batter'] == player_id]
        df1= player_frame.loc[player_frame['if_fielding_alignment'] == 'Strategic']
        mean = df1['launch_speed'].mean()
    
    elif (position == 2):
        player_frame = dataframe.loc[dataframe['batter'] == player_id]
        df1= player_frame.loc[player_frame['if_fielding_alignment'] == 'Infield shift']
        mean = df1['launch_speed'].mean()
       
    else:
        player_frame = dataframe.loc[dataframe['batter'] == player_id]
        mean = player_frame['launch_speed'].mean()
    return mean   
## gets the average launch angle for each player in frame at the same positions as above
def get_player_mean_la(player_id,dataframe, position = -1):
    if (position == 0):
        player_frame = dataframe.loc[dataframe['batter'] == player_id]
        df1= player_frame.loc[player_frame['if_fielding_alignment'] == 'Standard']
        mean = df1['launch_angle'].mean()
    
    elif (position == 1):
        player_frame = dataframe.loc[dataframe['batter'] == player_id]
        df1= player_frame.loc[player_frame['if_fielding_alignment'] == 'Strategic']
        mean = df1['launch_angle'].mean()
    
    elif (position == 2):
        player_frame = dataframe.loc[dataframe['batter'] == player_id]
        df1= player_frame.loc[player_frame['if_fielding_alignment'] == 'Infield shift']
        mean = df1['launch_angle'].mean()
       
    else:
        player_frame = dataframe.loc[dataframe['batter'] == player_id]
        mean = player_frame['launch_angle'].mean()
    return mean   

## calculates and returns a list of percentages of each if alignment faced for indicated player.. [standard,strategic,shift]     
def get_player_shift_list(player_id,dataframe):
    counter_standard=0
    counter_shift = 0
    counter_strat = 0
    player_list = dataframe.loc[dataframe['batter'] == player_id].reset_index(drop = True)
   # print(player_id , player_list.size)
    if (player_list.size == 0):
        return []
    for i in range(len(player_list.index)):
        row = player_list.iloc[[i]]
        if (row['if_fielding_alignment'].values[0]=='Standard'):
            counter_standard +=1
        elif (row['if_fielding_alignment'].values[0]=='Strategic'):
            counter_strat +=1            
        elif (row['if_fielding_alignment'].values[0]=='Infield shift'):
            counter_shift +=1    
   
    total = counter_standard + counter_shift  +  counter_strat
    
    ## some players faced ONLY one alignment which broke the above. Since we wanted to explore variences anyway,
    ## I just threw em out later
    try:
        return[counter_standard/total,counter_strat/total,counter_shift/total]
    except ZeroDivisionError:
        return []

    
    
    
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


batted_balls = pd.read_excel(r"raw_batted_balls.xlsx")
batted_balls = batted_balls.loc[batted_balls['launch_angle'] > 10]
player_info = batted_balls[['batter','stand']].drop_duplicates().reset_index(drop = True)

avgs_data = {'batter': [],  'bat_hand': [],'bip':[], 'wOBA_avg': [],'xwOBA_avg': [],'standard_wOBA_avg': [],'standard_xwOBA_avg': [], 'strat_wOBA_avg': [],'strat_xwOBA_avg': [], 'shift_wOBA_avg': [],'shift_xwOBA_avg': [], 'stadard_per': [],'strat_per': [],'shift_per': [], 'ev' : [], 'la':[],'ev_stand' : [], 'la_stand':[],'ev_strat' : [], 'la_strat':[],'ev_shift' : [], 'la_shift':[]}

## create a template for the data we care about

avgs_df_10 = pd.DataFrame(columns = ['batter', 'bat_hand','bip', 'wOBA_avg','xwOBA_avg','standard_wOBA_avg','standard_xwOBA_avg','strat_wOBA_avg',
                                  'strat_xwOBA_avg', 'shift_wOBA_avg','shift_xwOBA_avg', 'standard_per','strat_per','shift_per', 'ev', 'la','ev_stand',
                                  'la_stand','ev_strat', 'la_strat','ev_shift', 'la_shift'])

#runs through the players from the imported csv's above and calculates the dataframe values needed

for k in range(len(player_info.index+1)):
    if (k%100 == 0):
        print(str(round(k*100/len(player_info.index+1))) + '%')

    player = player_info.iloc[[k]].reset_index(drop = True)

    player_shift_list = get_player_shift_list(player.at[0,'batter'],batted_balls)
    if (player_shift_list == []):
        continue
    player_temp_dict = {'batter': [player.at[0,'batter']],
                        'bat_hand': [player.at[0,'stand']],
                        'bip': len(batted_balls.loc[batted_balls['batter']==player.at[0,'batter']].index),
                        'wOBA_avg': [get_player_mean_woba(player.at[0,'batter'],batted_balls)],
                        'xwOBA_avg': [get_player_mean_woba(player.at[0,'batter'],batted_balls, exp = True)],
                        'standard_wOBA_avg': [get_player_mean_woba(player.at[0,'batter'],batted_balls, position = 0)],
                        'standard_xwOBA_avg': [get_player_mean_woba(player.at[0,'batter'],batted_balls,exp = True, position = 0)],
                        'strat_wOBA_avg': [get_player_mean_woba(player.at[0,'batter'],batted_balls, position = 1)],
                        'strat_xwOBA_avg': [get_player_mean_woba(player.at[0,'batter'],batted_balls,exp = True, position = 1)],
                        'shift_wOBA_avg': [get_player_mean_woba(player.at[0,'batter'],batted_balls, position = 2)],
                        'shift_xwOBA_avg': [get_player_mean_woba(player.at[0,'batter'],batted_balls,exp = True, position = 2)],
                        'standard_per': [player_shift_list[0]],
                        'strat_per': [player_shift_list[1]],
                        'shift_per': [player_shift_list[2]],
                        'ev' : [get_player_mean_ev(player.at[0,'batter'],batted_balls)],
                        'la':[get_player_mean_la(player.at[0,'batter'],batted_balls)],
                        'ev_stand' : [get_player_mean_ev(player.at[0,'batter'],batted_balls,position =0)],
                        'la_stand':[get_player_mean_la(player.at[0,'batter'],batted_balls,position =0)],
                        'ev_strat' : [get_player_mean_ev(player.at[0,'batter'],batted_balls,position =1)],
                        'la_strat':[get_player_mean_la(player.at[0,'batter'],batted_balls,position =1)],
                        'ev_shift' : [get_player_mean_ev(player.at[0,'batter'],batted_balls,position =2)],
                        'la_shift':get_player_mean_la(player.at[0,'batter'],batted_balls,position =2)}
    player_temp_df = pd.DataFrame(player_temp_dict)
    avgs_df_10 = avgs_df_10.append(player_temp_df, ignore_index = True)
avgs_df_10 = avgs_df_10.dropna()

        


# writes the dataframe above to a an excel file
with pd.ExcelWriter(r"C:\Users\joedattoli\Desktop\ShiftScripts\batter_means_lamore10.xlsx") as writer:
    avgs_df_10.to_excel(writer)
    
#auto_run next script so I can leave for the day and not be behind
runpy.run_path(r'C:\Users\joedattoli\Desktop\ShiftScripts\together_splits_lamore10.py')