# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 08:19:49 2020

@author: joedattoli
"""
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb



###  IF YOU DOWNLOADED THIS FROM GITHUB TO EXPLORE, JUST CHANGE THE PATHS TO CORRESPONDING EXCEL FILES IN THE FOLDER
###  CONTACT ME FOR ANY QUESTIONS
### _la10 denotes a similar dataframe but with launch angle restrictions to no greater than 10 degrees
#batted_balls = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\raw_batted_balls.xlsx")
#batter_means = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\batter_means_file.xlsx")
#batter_means_la10 = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\batter_means_la10.xlsx")
#difference_woba = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\difference_woba.xlsx")
#difference_woba_la10 = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\difference_woba_la10.xlsx")
#mean_data_plus =  pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\mean_data_plus.xlsx")
#mean_data_plus_la10 =  pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\mean_data_plus_la10.xlsx")
zoned_batted_balls = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\zoned_batted_balls.xlsx")
zone_percent = pd.read_excel(r"C:\Users\joedattoli\Desktop\ShiftScripts\idea_machine.xlsx")


"""
difference_woba['wOBA - xwOBA'] = [x*-1 for x in difference_woba['wOBA - xwOBA']]
difference_woba_la10['wOBA - xwOBA'] = [x*-1 for x in difference_woba_la10['wOBA - xwOBA']]
"""
infield_pos_list = ['all','all','all','standard','standard','standard','strategic','strategic','strategic','shift','shift','shift']
handedness = ['B','L','R','B','L','R','B','L','R','B','L','R']




for i in range(len(zoned_batted_balls.index)):
    woba_list = [zoned_batted_balls['woba_value_all'][i],zoned_batted_balls['woba_value_L'][i],zoned_batted_balls['woba_value_R'][i],
              zoned_batted_balls['woba_value_standard'][i],zoned_batted_balls['woba_value_standard_L'][i],zoned_batted_balls['woba_value_standard_R'][i],
              zoned_batted_balls['woba_value_strategic'][i],zoned_batted_balls['woba_value_strategic_L'][i],zoned_batted_balls['woba_value_strategic_R'][i],
              zoned_batted_balls['woba_value_shift'][i],zoned_batted_balls['woba_value_shift_L'][i],zoned_batted_balls['woba_value_shift_R'][i]]

    xwoba_list = [zoned_batted_balls['estimated_woba_using_speedangle_all'][i], zoned_batted_balls['estimated_woba_using_speedangle_L'][i], zoned_batted_balls['estimated_woba_using_speedangle_R'][i], zoned_batted_balls['estimated_woba_using_speedangle_standard'][i], zoned_batted_balls['estimated_woba_using_speedangle_L'][i], zoned_batted_balls['estimated_woba_using_speedangle_standard_R'][i], zoned_batted_balls['estimated_woba_using_speedangle_strategic'][i], zoned_batted_balls['estimated_woba_using_speedangle_strategic_L'][i], zoned_batted_balls['estimated_woba_using_speedangle_strategic_R'][i],  zoned_batted_balls['estimated_woba_using_speedangle_shift'][i], zoned_batted_balls['estimated_woba_using_speedangle_shift_L'][i], zoned_batted_balls['estimated_woba_using_speedangle_shift_R'][i]]
    dif_list = [x-y for (x,y) in zip(woba_list,xwoba_list)]
    
    data_dict = {'infield_positioning' : infield_pos_list, 'handedness': handedness, 'woba': woba_list, 'xwoba': xwoba_list, 'woba-xwoba': dif_list}
    
    data_frame = pd.DataFrame(data_dict)
    
    
    
    
    
    dtf_woba_plot = sb.catplot(data =  data_frame, x='handedness', y='woba-xwoba', kind = 'bar', hue = 'infield_positioning')
    plt.title('wOBA difference in gameday zone ' + str(zoned_batted_balls['zone'][i]), pad = -20)
    #plt.ylim((.15,0.7))
    plt.ylabel('wOBA')
    plt.xlabel('Handedness')
    plt.show()

