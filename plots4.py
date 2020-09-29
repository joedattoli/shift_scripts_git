# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:19:49 2020

@author: joedattoli
"""
import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt

def combo_percentage(lst):
    onefourseven = 0
    threesixnine = 0
    middle = 0
    left_out = 0
    right_out = 0
    for i in range(len(lst)):
        if (i ==0 or i == 3 or i == 6):
            onefourseven += lst[i]
        elif(i ==2 or i == 5 or i == 8):
            threesixnine += lst[i]
        elif(i ==1 or i == 4 or i == 7):
            middle += lst[i]
        elif(i ==9 or i == 11):
            left_out += lst[i]        
        elif(i ==10 or i == 12):
            right_out += lst[i] 
        else:
            continue
    return [left_out,onefourseven,middle,threesixnine,right_out]
    
###  IF YOU DOWNLOADED THIS FROM GITHUB TO EXPLORE, JUST CHANGE THE PATHS TO CORRESPONDING EXCEL FILES IN THE FOLDER
###  CONTACT ME FOR ANY QUESTIONS
### _la10 denotes a similar dataframe but with launch angle restrictions to no greater than 10 degrees
#batted_balls = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\raw_batted_balls.xlsx")
#batter_means = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\batter_means_file.xlsx")
#batter_means_la10 = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\batter_means_la10.xlsx")
# difference_woba = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\difference_woba.xlsx")
# difference_woba_la10 = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\difference_woba_la10.xlsx")
# mean_data_plus =  pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\mean_data_plus.xlsx")
# mean_data_plus_la10 =  pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\mean_data_plus_la10.xlsx")
zone_percent = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\idea_machine.xlsx")

infield_pos_list = ['all','all','all','standard','standard','standard','strategic','strategic','strategic','shift','shift','shift']
handedness = ['B','L','R','B','L','R','B','L','R','B','L','R']
zones = zone_percent['Unnamed: 0']

zones = [round(x)for x in zones]
list_of_lists = [list(zone_percent['per']),list(zone_percent['per_L']),list(zone_percent['per_R']),
                 list(zone_percent['per_standard']),list(zone_percent['per_standard_L']),list(zone_percent['per_standard_R']),
                 list(zone_percent['per_strategic']),list(zone_percent['per_strategic_L']),list(zone_percent['per_strategic_R']),
                 list(zone_percent['per_shift']),list(zone_percent['per_shift_L']),list(zone_percent['per_shift_R'])]

zone_qual_list = ['11,13', '1,4,7', '2,5,8','3,6,9','12,14']


for i in range(len(list_of_lists)):
    df= pd.DataFrame({'zone': zone_qual_list, 'infield_positioning': [infield_pos_list[i] for k in range(5)], 'handedness': [handedness[i] for k in range(5)], 'zone_percent': combo_percentage(list_of_lists[i])})
    
    
    dtf_woba_plot = sb.catplot(data =  df, x='zone', y='zone_percent', kind = 'bar', palette= 'icefire' )
    plt.title('Zone percentage for ' + str(df['handedness'][0]) + " batter and " + str(df['infield_positioning'][0]), pad = -20)
    plt.ylim((0,0.4))
    plt.ylabel('% balls thrown in zone')
    plt.xlabel('Zone')
    plt.show()
    
    #print(df['handedness'][0],df['infield_positioning'][0],list(df['zone_percent']))





