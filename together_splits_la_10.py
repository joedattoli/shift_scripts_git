# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:26:49 2020

@author: joedattoli
"""

## Same As Together Splits but with a file that only allows a launch angle of 10 or less
##expands the list of percentages to whole number of bips facing a certain alignment
import pandas as pd 
import numpy as np



def shift_expand(bip,small_frame):
    per_list = [list(small_frame['standard_per'].values),list(small_frame['strat_per'].values),list(small_frame['shift_per'].values)]
    stand = bip*per_list[0]
    strat = bip*per_list[1]
    shift = bip*per_list[2]
    return[stand[0],strat[0],shift[0]]
def weighted_mean_woba(dataframe):
    count_stand=[]
    count_strat=[]
    count_shift=[]
    together=[]
    for i in range(len(dataframe.index)):
        player = dataframe.iloc[[i]].reset_index(drop = True)
        tup = shift_expand(player['bip'],player[['standard_per','strat_per','shift_per']])
        count_stand.append(tup[0])
        count_strat.append(tup[1])
        count_shift.append(tup[2])
        together.append(player['bip'][0])
    
    tup2 = (np.average(np.array(dataframe['standard_wOBA_avg']),weights = count_stand),np.average(np.array(dataframe['strat_wOBA_avg']),weights = count_strat),np.average(np.array(dataframe['shift_wOBA_avg']),weights = count_shift), np.average(np.array(dataframe['wOBA_avg']),weights = together))
    return tup2

        
# actuallly calcultes the weighted mean of the xwobas
def weighted_mean_xwoba(dataframe):
    count_stand=[]
    count_strat=[]
    count_shift=[]
    together=[]
    for i in range(len(dataframe.index)):
        player = dataframe.iloc[[i]].reset_index(drop = True)
        tup = shift_expand(player['bip'],player[['standard_per','strat_per','shift_per']])
        count_stand.append(tup[0])
        count_strat.append(tup[1])
        count_shift.append(tup[2])
        together.append(player['bip'][0])
        
    tup2 = (np.average(np.array(dataframe['standard_xwOBA_avg']),weights = count_stand),np.average(np.array(dataframe['strat_xwOBA_avg']),weights = count_strat),np.average(np.array(dataframe['shift_xwOBA_avg']),weights = count_shift), np.average(np.array(dataframe['xwOBA_avg']),weights = together))
    return tup2

# actuallly calculates the weighted mean of the exit velocity
def weighted_mean_ev(dataframe):
    count_stand=[]
    count_strat=[]
    count_shift=[]
    together=[]
    for i in range(len(dataframe.index)):
        player = dataframe.iloc[[i]].reset_index(drop = True)
        tup = shift_expand(player['bip'],player[['standard_per','strat_per','shift_per']])
        count_stand.append(tup[0])
        count_strat.append(tup[1])
        count_shift.append(tup[2])
        together.append(player['bip'][0])
        
        
    tup2 = (np.average(dataframe['ev_stand'],weights = count_stand),np.average(dataframe['ev_strat'],weights = count_strat),np.average(dataframe['ev_shift'],weights = count_shift), np.average(np.array(dataframe['ev']),weights = together))
    return tup2

# actuallly calculates the weighted mean of the launch angle
def weighted_mean_la(dataframe):
    count_stand=[]
    count_strat=[]
    count_shift=[]
    together=[]
    for i in range(len(dataframe.index)):
        player = dataframe.iloc[[i]].reset_index(drop = True)
        tup = shift_expand(player['bip'],player[['standard_per','strat_per','shift_per']])
        count_stand.append(tup[0])
        count_strat.append(tup[1])
        count_shift.append(tup[2])
        together.append(player['bip'][0])
        
        
    tup2 = (np.average(dataframe['la_stand'],weights = count_stand),np.average(dataframe['la_strat'],weights = count_strat),np.average(dataframe['la_shift'],weights = count_shift), np.average(np.array(dataframe['la']),weights = together))
    return tup2

#normalizes the averages and sets the base to 100. Similar to the usual + stats
def norm_plus(dataframe):
    cols = dataframe.columns
    for col in cols:
        if (col == 'def_pos'):
            continue
        ary = dataframe[col]
        norm_factor = ary[3]
        new_col = [x/norm_factor*100 for x in ary]
        dataframe[col+'+'] = new_col 
    return dataframe

#finds the differece between the specified columns below.
def difference_maker (dataframe):
    col_pairs = [['wmw','wmxw'],['wmw_L','wmxw_L'],['wmw_R','wmxw_R']]
    new_col_list = ['def_pos', 'wOBA - xwOBA' , 'wOBA_lefty - xwOBA_lefty', 'wOBA_righty - xwOBA_righty']
    new_frame = pd.DataFrame(columns = new_col_list)
    new_frame['def_pos'] = dataframe['def_pos']
    
    for k in range(len(col_pairs)):
        pair = col_pairs[k]
        list1 = dataframe[pair[0]]
        list2 = dataframe[pair[1]]
        new_col = [x - y for x,y in zip(list1,list2)]
        new_frame[new_col_list[k+1]] = new_col
    ## for plots, we need them frame in a different format
    ## the rest of the function after this comment is an updated version
    ## kinda like a band aid repair
    
    old_list = ['wOBA - xwOBA' , 'wOBA_lefty - xwOBA_lefty', 'wOBA_righty - xwOBA_righty']
    dif_list = []
    hand_list=[]
    def_pos_list =[]
    for i in range(len(new_frame.index)):
        old_col = new_frame.iloc[[i]]
        
        for n in range(len(old_list)):
            if (n == 1):
                dif_list.append([old_col['wOBA_lefty - xwOBA_lefty'].values[0]][0])
                hand_list.append('L')
                def_pos_list.append([old_col['def_pos'].values[0]][0])

            elif (n == 2):
                dif_list.append([old_col['wOBA_righty - xwOBA_righty'].values[0]][0])
                hand_list.append('R')
                def_pos_list.append([old_col['def_pos'].values[0]][0])
            else:
                dif_list.append([old_col['wOBA - xwOBA'].values[0]][0])
                hand_list.append('B')
                def_pos_list.append([old_col['def_pos'].values[0]][0])
    edit_axis_frame = pd.DataFrame({'def_pos': def_pos_list,'handedness': hand_list,'wOBA - xwOBA':dif_list})       
    return edit_axis_frame
    
##reads the data calculated from by_player.py and only takes guys meeting certain thresholds 
## Since we are now just focused in on LA <=10, we can drop the BIP of 100 reqs to 75, shift percentage remains the same
batter_means = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\batter_means_la10.xlsx")
batter_means = batter_means.loc[batter_means['bip'] >= 200]
batter_means = batter_means.loc[batter_means['shift_per'] >= 0.25]
## creates two more frames of only right handed and left handed batters
batter_means_L=batter_means.loc[batter_means['bat_hand']=='L']
batter_means_R=batter_means.loc[batter_means['bat_hand']=='R']

##runs through the functions and gets means
wmw = weighted_mean_woba(batter_means)
wmxw = weighted_mean_xwoba(batter_means)
wmev=weighted_mean_ev(batter_means)
wmla= weighted_mean_la(batter_means)

##runs through the functions and gets means
wmw_L = weighted_mean_woba(batter_means_L)
wmxw_L = weighted_mean_xwoba(batter_means_L)
wmev_L =weighted_mean_ev(batter_means_L)
wmla_L = weighted_mean_la(batter_means_L)

##runs through the functions and gets means
wmw_R = weighted_mean_woba(batter_means_R)
wmxw_R = weighted_mean_xwoba(batter_means_R)
wmev_R =weighted_mean_ev(batter_means_R)
wmla_R = weighted_mean_la(batter_means_R)

##creates a dictionary and seperates by handedness and infield alignment
data_dict = {'def_pos': ['standard','strategic','shift','together'],'wmw': [wmw[0],wmw[1],wmw[2],wmw[3]] , 'wmxw' : [wmxw[0],wmxw[1],wmxw[2],wmxw[3]], 'wmev': [wmev[0],wmev[1],wmev[2],wmev[3]] , 'wmla': [wmla[0],wmla[1],wmla[2],wmla[3]],'wmw_L': [wmw_L[0],wmw_L[1],wmw_L[2],wmw_L[3]] , 'wmxw_L' : [wmxw_L[0],wmxw_L[1],wmxw_L[2],wmxw_L[3]], 'wmev_L': [wmev_L[0],wmev_L[1],wmev_L[2],wmev_L[3]] , 'wmla_L': [wmla_L[0],wmla_L[1],wmla_L[2],wmla_L[3]], 'wmw_R': [wmw_R[0],wmw_R[1],wmw_R[2],wmw_R[3]] , 'wmxw_R' : [wmxw_R[0],wmxw_R[1],wmxw_R[2],wmxw_R[3]], 'wmev_R': [wmev_R[0],wmev_R[1],wmev_R[2],wmev_R[3]] , 'wmla_R': [wmla_R[0],wmla_R[1],wmla_R[2],wmla_R[3]]}


#puts the dictionary into a dataframe
data_frame = pd.DataFrame(data_dict)

#normalizes the data
data_frame_normed_10 = norm_plus(data_frame)

#makes a dataframe of the differences between actual wOBA and xwOBA based on EV and LA
dif_frame_10 = difference_maker(data_frame)

print('line 176 2nd')
##puts the normed frame and difference frame into two excel files
with pd.ExcelWriter(r"C:\Users\joedattoli\Desktop\ShiftScripts\difference_woba_la10.xlsx") as writer:
    dif_frame_10.to_excel(writer)
with pd.ExcelWriter(r"C:\Users\joedattoli\Desktop\ShiftScripts\mean_data_plus_la10.xlsx") as writer:
    data_frame_normed_10.to_excel(writer)

    
#auto_run next script so I can leave for the day and not be behind
