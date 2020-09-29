# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:39:05 2020

@author: joedattoli
"""

import os
import pandas as pd 
import glob
import runpy
    
def get_zone_per(series):
    total=0
    series_prime = series.astype('float')
    for index in series.index:
        total += series[index]
    for index in series.index:    
        
        series_prime[index] = series[index]/total
    return series_prime
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

pitches1 = pd.read_excel(r"test_test_test_raw_pitches_1.xlsx")
pitches2 = pd.read_excel(r"test_test_test_raw_pitches_2.xlsx")

pitches = pd.concat([pitches1,pitches2])


pitches_L = pitches.loc[pitches['stand']== 'L']
pitches_R = pitches.loc[pitches['stand']== 'R']

pitches_stand = pitches.loc[pitches['if_fielding_alignment']== 'Standard']
pitches_strat = pitches.loc[pitches['if_fielding_alignment']== 'Strategic']
pitches_shift = pitches.loc[pitches['if_fielding_alignment']== 'Infield shift']

pitches_stand_L = pitches_L.loc[pitches_L['if_fielding_alignment']== 'Standard']
pitches_strat_L = pitches_L.loc[pitches_L['if_fielding_alignment']== 'Strategic']
pitches_shift_L = pitches_L.loc[pitches_L['if_fielding_alignment']== 'Infield shift']

pitches_stand_R = pitches_R.loc[pitches_R['if_fielding_alignment']== 'Standard']
pitches_strat_R = pitches_R.loc[pitches_R['if_fielding_alignment']== 'Strategic']
pitches_shift_R = pitches_R.loc[pitches_R['if_fielding_alignment']== 'Infield shift']


description_counts = pitches['description'].value_counts()
zone_counts = pitches['zone'].value_counts()
zone_counts_standard = pitches_stand['zone'].value_counts()
zone_counts_strategic = pitches_strat['zone'].value_counts()
zone_counts_shift = pitches_shift['zone'].value_counts()

zone_counts_L = pitches_L['zone'].value_counts()
zone_counts_standard_L = pitches_stand_L['zone'].value_counts()
zone_counts_strategic_L = pitches_strat_L['zone'].value_counts()
zone_counts_shift_L = pitches_shift_L['zone'].value_counts()



zone_counts_R = pitches_R['zone'].value_counts()
zone_counts_standard_R = pitches_stand_R['zone'].value_counts()
zone_counts_strategic_R = pitches_strat_R['zone'].value_counts()
zone_counts_shift_R = pitches_shift_R['zone'].value_counts()



ozone_total = zone_counts[14]+zone_counts[13]+zone_counts[12]+zone_counts[11]
izone_total = zone_counts[1]+zone_counts[2]+zone_counts[3]+zone_counts[4]+zone_counts[5]+zone_counts[6]+zone_counts[7]+zone_counts[8]+zone_counts[9]

ozone_total_standard = zone_counts_standard[14]+zone_counts_standard[13]+zone_counts_standard[12]+zone_counts_standard[11]
izone_total_standard = zone_counts_standard[1]+zone_counts_standard[2]+zone_counts_standard[3]+zone_counts_standard[4]+zone_counts_standard[5]+zone_counts_standard[6]+zone_counts_standard[7]+zone_counts_standard[8]+zone_counts_standard[9]


#ozone_total_strategic = zone_counts_strategic[14]+zone_counts_strategic[13]+zone_counts_strategic[12]+zone_counts_strategic[11]
#izone_total_strategic = zone_counts_strategic[1]+zone_counts_strategic[2]+zone_counts_strategic[3]+zone_counts_strategic[4]+zone_counts_strategic[5]+zone_counts_strategic[6]+zone_counts_strategic[7]+zone_counts_strategic[8]+zone_counts_strategic[9]


ozone_total_shift = zone_counts_shift[14]+zone_counts_shift[13]+zone_counts_shift[12]+zone_counts_shift[11]
izone_total_shift = zone_counts_shift[1]+zone_counts_shift[2]+zone_counts_shift[3]+zone_counts_shift[4]+zone_counts_shift[5]+zone_counts_shift[6]+zone_counts_shift[7]+zone_counts_shift[8]+zone_counts_shift[9]

izone = izone_total / (izone_total + ozone_total)
izone_standard = izone_total_standard / (izone_total_standard + ozone_total_standard)
#izone_strategic = izone_total_strategic / (izone_total_strategic + ozone_total_strategic)
izone_shift = izone_total_shift / (izone_total_shift + ozone_total_shift)


zone_per = get_zone_per(zone_counts)
zone_per_standard = get_zone_per(zone_counts_standard)
zone_per_strategic = get_zone_per(zone_counts_strategic)
zone_per_shift = get_zone_per(zone_counts_shift)

zone_per_L = get_zone_per(zone_counts_L)
zone_per_standard_L = get_zone_per(zone_counts_standard_L)
zone_per_strategic_L = get_zone_per(zone_counts_strategic_L)
zone_per_shift_L = get_zone_per(zone_counts_shift_L)

zone_per_R = get_zone_per(zone_counts_R)
zone_per_standard_R = get_zone_per(zone_counts_standard_R)
zone_per_strategic_R = get_zone_per(zone_counts_strategic_R)
zone_per_shift_R = get_zone_per(zone_counts_shift_R)

zone_per = zone_per.sort_index()
zone_per_standard = zone_per_standard.sort_index()
zone_per_strategic =zone_per_strategic.sort_index()
zone_per_shift = zone_per_shift.sort_index()

zone_per_L =zone_per_L.sort_index()
zone_per_standard_L = zone_per_standard_L.sort_index()
zone_per_strategic_L = zone_per_strategic_L.sort_index()
zone_per_shift_L = zone_per_shift_L.sort_index()

zone_per_R = zone_per_R.sort_index()
zone_per_standard_R = zone_per_standard_R.sort_index()
zone_per_strategic_R = zone_per_strategic_R.sort_index()
zone_per_shift_R = zone_per_shift_R.sort_index()

zone_per_frame = pd.concat([zone_per,zone_per_standard,zone_per_strategic,zone_per_shift,zone_per_L,zone_per_standard_L,zone_per_strategic_L,zone_per_shift_L,
                            zone_per_R,zone_per_standard_R,zone_per_strategic_R,zone_per_shift_R])


big_list = [zone_per,zone_per_standard,zone_per_strategic,zone_per_shift,zone_per_L,zone_per_standard_L,zone_per_strategic_L,zone_per_shift_L,
                            zone_per_R,zone_per_standard_R,zone_per_strategic_R,zone_per_shift_R]
col_list = ['zone','per','per_standard','per_strategic','per_shift','per_L','per_standard_L','per_strategic_L','per_shift_L',
            'per_R','per_standard_R','per_strategic_R','per_shift_R']
big_frame_zone = pd.DataFrame(columns = col_list )

for i in range(len(col_list)):
    if col_list[i] == 'zone':
        continue

    big_frame_zone[col_list[i]]= big_list[i-1]
    
    

with pd.ExcelWriter(r"C:\Users\joedattoli\Desktop\ShiftScripts\idea_machine.xlsx") as writer:
    big_frame_zone.to_excel(writer)

