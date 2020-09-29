# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:19:49 2020

@author: joedattoli
"""
import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt


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
"""
difference_woba['wOBA - xwOBA'] = [x*-1 for x in difference_woba['wOBA - xwOBA']]
difference_woba_la10['wOBA - xwOBA'] = [x*-1 for x in difference_woba_la10['wOBA - xwOBA']]
"""


dif_woba_plot = sb.catplot(data = difference_woba, x='handedness', y='wOBA - xwOBA', kind = 'bar', hue = 'def_pos')
plt.title('wOBA  Difference', pad = -20)
plt.ylabel('wOBA - xWOBA')
plt.xlabel('Handedness')
plt.show()


dif_la10_woba_plot = sb.catplot(data = difference_woba_la10, x='handedness', y='wOBA - xwOBA', kind = 'bar', hue = 'def_pos')
plt.title('wOBA  Difference For LA 10 or Less', pad = -20)
plt.ylabel('wOBA - xWOBA')
plt.xlabel('Handedness')
plt.show()

dif_lamore10_woba_plot = sb.catplot(data = difference_woba_lamore10, x='handedness', y='wOBA - xwOBA', kind = 'bar', hue = 'def_pos')
plt.title('wOBA  Difference For LA Over 10', pad = -20)
plt.ylabel('wOBA - xWOBA')
plt.xlabel('Handedness')
plt.show()




