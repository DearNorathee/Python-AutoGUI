# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:41:29 2023

@author: Heng2020
"""
# for developing functions and other utilities

import pyautogui as pgu
import pyscreeze as psc
import sys

sys.path.append(r"C:\Users\Heng2020\OneDrive\Python MyLib")

import ungroupped02 as f2

def cap_num(number,lower_bound, upper_bound):
    # medium tested
    ans = max(min(number, upper_bound), lower_bound)
    return ans

def pgu_double_click(image_path, confidence = None):
    # medium tested
    if confidence:
        image_pos = pgu.locateCenterOnScreen(image_path,confidence=confidence)
    else:
        image_pos = pgu.locateCenterOnScreen(image_path)
    
    if image_pos is None:
        print("Nothing is clicked")
        
    pgu.doubleClick(image_pos)

def pgu_single_click(image_path, confidence = None):
    # medium tested
    
    if confidence:
        image_pos = pgu.locateCenterOnScreen(image_path,confidence=confidence)
    else:
        image_pos = pgu.locateCenterOnScreen(image_path)
        
    if image_pos is None:
        print("Nothing is clicked")
    pgu.click(image_pos)

def psc_add_x(box_object, added_x):
    # medium tested
    import pyscreeze as psc
    # x could be negative
    screen_width, screen_height = pgu.size()
    x, y, width, height = box_object
    
    new_x = x + added_x
    new_y = cap_num(new_x, 0, screen_width)
    
    out_box = psc.Box(new_x, y, width, height)
    return out_box

def psc_add_y(box_object, added_y):
    # medium tested
    import pyscreeze as psc
    
    screen_width, screen_height = pgu.size()
    x, y, width, height = box_object
    new_y = y + added_y
    
    new_y = cap_num(new_y, 0, screen_height)
    
    out_box = psc.Box(x, new_y, width, height)
    return out_box

def psc_add_width(box_object, added_width):
    # medium tested
    import pyscreeze as psc
    
    screen_width, screen_height = pgu.size()
    x, y, width, height = box_object
    new_width = width + added_width
    out_box = psc.Box(x, y, new_width, height)
    return out_box

def psc_add_height(box_object, added_height):
    # medium tested
    import pyscreeze as psc
    screen_width, screen_height = pgu.size()
    
    x, y, width, height = box_object
    new_height = height + added_height
    out_box = psc.Box(x, y, width, new_height)
    return out_box

def _conf_boolen(image_path, correct_x = None, correct_y = None, tolerance = 0.07):
    # medium tested
    # helper function that is used in  find_confidence, confidence_range
    # avoid repeated code
    condition = (correct_x and not correct_y)  or (not correct_x and correct_y)
    
    diff_list = []
    # range only accepts integer
    conf_list = [conf/100 for conf in range(50,101)]
    
    if (correct_x and not correct_y)  or (not correct_x and correct_y):
        print("Only allow both None's or both numbers. Can't handle when only 1 is None")
    elif (correct_x and correct_y):
        for conf in conf_list:
            box= pgu.locateCenterOnScreen(image_path, confidence=conf)
            
            if box is not None:
                locate_x, locate_y = box
                
                if condition:
                    pass
                else:
                    diff = (locate_x/correct_x)-1
                    if abs(diff) < tolerance:
                        diff_list.append(True)
                    else:
                        diff_list.append(False)
            else:
                diff_list.append(False)
                
    elif (correct_x is None) and (correct_y is None):
        
        for conf in conf_list:
            box= pgu.locateCenterOnScreen(image_path, confidence=conf)
            
            if box is not None:
                diff_list.append(True)
            else:
                diff_list.append(False)
    return diff_list

def change_value_index(lst,change_from = False, change_to = True):
    # medium tested via: confidence_range
    index_list = []
    
    for i in range(len(lst)-1):
        if (lst[i] == change_from) and (lst[i+1] == change_to):
            index_list.append(i)
    
    if len(index_list) == 0:
        return "Can't find any changes"
    elif len(index_list) == 1:
        # return as single value
        return index_list[0]
    else:
        return index_list
    
    

def find_confidence(image_path, correct_x = None, correct_y = None, tolerance = 0.07):
    # medium tested
    
    # the return the max confidence that will make the image search valid 
    # tolerance is the diff that I could considered True
    # if higher than tolerance then it's not the same box I'm looking for
    
    # enhance01: add epoch = 10(check only 10 times to reduce the number checking and speed
    # up the code
    # is the avg between low and high confidence
    
    # if conf is too slow, it will detect wrong/other region
    # if conf is too high, it can't detect something at all because it's too strict
    warn_msg = "Make sure that no windows is on top of the image you want to search"
    
    conf_values = [conf/100 for conf in range(50,101)]
    
    try:
        # slow here: _conf_boolen
        min_conf, max_conf = confidence_range(image_path,correct_x,correct_y,tolerance)
        ans = round( (min_conf+max_conf)/2 , 2)
    except:
        return warn_msg
    return ans
        
def confidence_range(image_path, correct_x = None, correct_y = None, tolerance = 0.07):
    # medium tested
    # if we set the 
    
    conf_values = [conf/100 for conf in range(50,101)]
    
    diff_list = _conf_boolen(image_path,correct_x,correct_y,tolerance)
    
    min_index = change_value_index(diff_list,False,True)
    
    if isinstance(min_index, str) and diff_list[0]:
        min_index = 0
    # what about case where there are all true?
    # very unlikely
    max_index = change_value_index(diff_list,True,False)
    
    warn_msg = "Make sure that no windows is on top of the image you want to search"
    try:
        ans = [conf_values[min_index],conf_values[max_index]]
    except:
        print(warn_msg)
        return warn_msg
    
    return ans


def position_from_text(text):
    import pyautogui as pgu
    from pytesseract import Output
    from PIL import Image
    import pytesseract
    import os

    screenshot = pgu.screenshot()

    # Save the screenshot as an image file
    screenshot.save('screenshot.png')

    # Open the saved screenshot image using PIL
    image = Image.open('screenshot.png')

    df_ocr = pytesseract.image_to_data(image, output_type=Output.DATAFRAME)

    mask = df_ocr['text'].str.contains(text,case=False,na=False)
    
    row_found = df_ocr[mask].reset_index()
    
    # remove screenshot temp file
    os.remove('screenshot.png')
    
    if len(row_found) == 1:
        # assume that only 1 row found
        pos_left = row_found.loc[0,'left']
        pos_top = row_found.loc[0,'top']
        pos_width = row_found.loc[0,'width']
        pos_height = row_found.loc[0,'height']
    
        center_x = pos_left + (pos_width/2)
        center_y = pos_top + (pos_height/2)
        
        return [center_x,center_y]
    elif len(row_found) == 0:
        
        print("No text found !!!!")
        return False
    

def pgu_click_from_text(text):
    center_x, center_y = position_from_text(text)
    pgu.click(center_x,center_y)


def screen_shot(output_name,monitor ):
    # number based on my computer
    import mss
    import mss.tools
    
    if isinstance(monitor,str):
        if monitor == "left":
            monitor_number = 1
        elif monitor in ["right","main"]:
            monitor_number = 2
        elif monitor == "all":
            monitor_number = 0
    elif isinstance(monitor_number,int):
        monitor_number = monitor
    with mss.mss() as sct:
        # Get information of monitor 2
        
        monitor_info = sct.monitors
        select_monitor = monitor_info[monitor_number]
    
        # The screen part to capture
        monitor_dict = {
            "top": select_monitor["top"],
            "left": select_monitor["left"],
            "width": select_monitor["width"],
            "height": select_monitor["height"],
            "mon": monitor_number,
        }
        output = f"{output_name}.png"
    
        # Grab the data
        sct_img = sct.grab(monitor_dict)
    
        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

def test_screen_shot():
    screen_shot("all_screen", "all")
    screen_shot("left_screen", "left")
    screen_shot("right_screen", "right")
    # screen_shot("all_screen", "all")

    
            
