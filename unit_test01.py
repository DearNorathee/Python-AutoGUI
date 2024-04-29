# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:40:03 2023

@author: Heng2020
"""
# testing for auto_GUI01.py

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:41:29 2023

@author: Heng2020
"""
# for developing functions and other utilities

import pyautogui as pgu
import pyscreeze as psc
import sys
import auto_GUI01 as agu
sys.path.append(r"C:\Users\Heng2020\OneDrive\Python MyLib")

import ungroupped02 as f2


# func_list = f2.obj_function(pgu)

# agu.pgu_double_click("pic04_VBAColorFolder.PNG")
# agu.pgu_single_click("pic05_Maximize.PNG")

agu.find_confidence("pic04_VBAColorFolder.PNG",766,1174)
agu.confidence_range("pic04_VBAColorFolder.PNG",766,1174)

# test = pgu.locateCenterOnScreen("pic04_VBAColorFolder.PNG", confidence=0.88)
# pgu.moveTo(test)
# test02 = pgu.locateAllOnScreen("pic04_VBAColorFolder.PNG", confidence=0.9)

test03 = [x for x in test02]
# agu.pgu_double_click("pic08_PathFile.png")

# path_file = pgu.locateCenterOnScreen("pic08_PathFile.png", confidence= 0.7)

# pgu.moveTo(path_file)


# end_line_pos = pgu.locateCenterOnScreen("pic12_EndLine1.PNG", confidence= 0.5)
# end_line_pos_ori = pgu.locateOnScreen("pic12_EndLine1.PNG", confidence= 0.5)