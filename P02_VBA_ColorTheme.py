# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:17:10 2023

@author: Heng2020
"""
import pyautogui as pgu
import pyscreeze as psc
import sys

import auto_GUI01 as agu
sys.path.append(r"C:\Users\Heng2020\OneDrive\Python MyLib")
import time
import ungroupped02 as f2

# pgu.typewrite(text)

# func_list = f2.obj_function(pgu)

agu.pgu_double_click("pic04_VBAColorFolder.PNG")
# what if it opens in other screen
# right now assuming it's the correct screen
agu.pgu_single_click("pic05_Maximize.PNG")

agu.find_confidence("pic08_PathFile.png")
# agu.confidence_range("pic08_PathFile.png")

agu.pgu_double_click("pic08_PathFile.png", confidence= 0.72)

agu.pgu_single_click("pic12_EndLine1.PNG",confidence= 0.7)
pgu.hotkey("Ctrl","right")
# pgu.hotkey("shift","home")
time.sleep(0.2) 
pgu.keyDown('shift')
time.sleep(0.2) 
pgu.press('home')
# pgu.keyUp('shift')

path_file = pgu.locateCenterOnScreen("pic08_PathFile.png", confidence= 0.7)
pgu.hotkey()
pgu.moveTo(path_file)


end_line_pos = pgu.locateCenterOnScreen("pic12_EndLine1.PNG", confidence= 0.5)
end_line_pos_ori = pgu.locateOnScreen("pic12_EndLine1.PNG", confidence= 0.5)










