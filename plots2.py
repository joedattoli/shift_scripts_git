# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:19:49 2020

@author: joedattoli
"""
import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt

def dtf(dataframe):
    def_pos_list = []
    wOBA_list = []
    xwOBA_list = []
    hand_list = []
    for i in range(3):
        for k in range(4):
            def_pos_list.append(dataframe['def_pos'][k])
            if i == 0: 
                wOBA_list.append(dataframe['wmw'][k])
                xwOBA_list.append(dataframe['wmxw'][k])
                hand_list.append('B')
            elif i == 1: 
                wOBA_list.append(dataframe['wmw_L'][k])
                xwOBA_list.append(dataframe['wmxw_L'][k])
                hand_list.append('L')
            elif i == 2:
                wOBA_list.append(dataframe['wmw_R'][k])
                xwOBA_list.append(dataframe['wmxw_R'][k])
                hand_list.append('R')
                
    dtf = pd.DataFrame({'def_pos':def_pos_list,'xwOBA':xwOBA_list,'wOBA':wOBA_list,'hand':hand_list})
    return dtf






###  IF YOU DOWNLOADED THIS FROM GITHUB TO EXPLORE, JUST CHANGE THE PATHS TO CORRESPONDING EXCEL FILES IN THE FOLDER
###  CONTACT ME FOR ANY QUESTIONS
### _la10 denotes a similar dataframe but with launch angle restrictions to no greater than 10 degrees
#batted_balls = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\raw_batted_balls.xlsx")
#batter_means = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\batter_means_file.xlsx")
#batter_means_la10 = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\batter_means_la10.xlsx")
difference_woba = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\difference_woba.xlsx")
difference_woba_la10 = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\difference_woba_la10.xlsx")
mean_data_plus =  pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\mean_data_plus.xlsx")
mean_data_plus_la10 =  pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\mean_data_plus_la10.xlsx")
difference_woba_lamore10 = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\difference_woba_lamore10.xlsx")
mean_data_plus_lamore10 =  pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\mean_data_plus_lamore10.xlsx")

dataframe = dtf(mean_data_plus)
dataframe10 = dtf(mean_data_plus_la10)
dataframelamore10 = dtf(mean_data_plus_lamore10)

dtf_woba_plot = sb.catplot(data = dataframe, x='hand', y='wOBA', kind = 'bar', hue = 'def_pos')
plt.title('wOBA given up', pad = -20)
plt.ylim((0.15,0.5))
plt.ylabel('wOBA')
plt.xlabel('Handedness')
plt.show()

dtf_woba_plot = sb.catplot(data =  dataframe, x='hand', y='xwOBA', kind = 'bar', hue = 'def_pos')
plt.title('xwOBA given up', pad = -20)
plt.ylim((0.15,0.5))
plt.ylabel('xWOBA')
plt.xlabel('Handedness')
plt.show()

dtf_woba_plot = sb.catplot(data =  dataframe10, x='hand', y='wOBA', kind = 'bar', hue = 'def_pos')
plt.title('wOBA given up, LA < 10', pad = -20)
plt.ylim((.15,0.5))
plt.ylabel('wOBA')
plt.xlabel('Handedness')
plt.show()

dtf_woba_plot = sb.catplot(data =  dataframe10, x='hand', y='xwOBA', kind = 'bar', hue = 'def_pos')
plt.title('xwOBA given up LA < 10', pad = -20)
plt.ylim((0.15,0.5))
plt.ylabel('xWOBA')
plt.xlabel('Handedness')
plt.show()






