# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:18:14 2023

@author: Heng2020
"""
import pyautogui as pgu

# text_location = pgu.locateCenterOnScreen("pic02.PNG")
# print(text_location)
# pos_x, pos_y = text_location
bar_down_y = 1418

folder_top_y = 344
folder_bottom_y = 569

folder_increment = 25
excel_increment = 25

excel_A1_y = 388
excel_A10_y = 607



# # pgu.press("F2")

# pgu.hotkey("F2")
# pgu.hotkey("Ctrl","C")

# # Excel icon
# pgu.moveTo(794,bar_down_y)
# pgu.click()

# pgu.hotkey("Ctrl","V")

n_folder = 10

for i in range(n_folder):
    # Folder icon
    folder_icon_x, folder_icon_y = [509,bar_down_y]
    pgu.moveTo(folder_icon_x,folder_icon_y)
    pgu.click()
    
    
    curr_y = folder_top_y + i*folder_increment
    pgu.moveTo(470,curr_y)
    pgu.click()
    
    pgu.hotkey("F2")
    pgu.hotkey("Ctrl","C")
    
    # Excel icon
    pgu.moveTo(794,bar_down_y)
    pgu.click()
    
    #move to cell in Excel
    curr_cell_y = excel_A1_y + i*excel_increment
    pgu.moveTo(78,curr_cell_y)
    pgu.click()
    
    pgu.hotkey("Ctrl","V")
    
    
    
    


