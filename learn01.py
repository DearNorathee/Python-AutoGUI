# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 10:08:07 2023

@author: Heng2020
"""
import pyautogui as pgu
from pytesseract import Output
Output.DATAFRAME
from typing import Literal
print(pgu.position())


screen_image = pgu.screenshot()

# Convert the screenshot image to grayscale
gray_image = screen_image.convert('L')

# Define the text to search for
text_to_search = "TypeError: '>' not supported between instances"

# Search for the text within the image
text_location = pgu.locateOnScreen("pic03_FolderIcon.PNG")
print(text_location)
# pos_x, pos_y,_,_ = text_location

# pos_x = 1211
# pos_y = 1055.6
# pgu.moveTo(pos_x,pos_y)

############ Search text on the screen and click on it ########################
################## Is very difficult for now 
# I manged to OCR using pytesseract for individual letters and I need to put them together into sentences
from PIL import Image
import pytesseract


# how to setup pytesseract
# https://www.youtube.com/watch?v=PY_N1XdFp4w&ab_channel=NeuralNine

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



output_name = "right_screen"
monitor_number = 1
test_screen_shot()




center_x, center_y = position_from_text("Overtone")
pgu.click(center_x,center_y)
pgu.moveTo(-1150,683)
pgu_click_from_text("Overtone")

screenshot = pgu.screenshot()

# Save the screenshot as an image file
screenshot.save('screenshot.png')

# Open the saved screenshot image using PIL
image = Image.open('screenshot.png')

# Perform OCR using pytesseract
# text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')

# data = pytesseract.image_to_boxes(image)
# this part will take long
data2 = pytesseract.image_to_data(image, output_type=Output.DATAFRAME)

text = "Overtone"
mask = data2['text'].str.contains(text,case=False,na=False)
row_found = data2[mask].reset_index()

# assume that only 1 row found
pos_left = row_found.loc[0,'left']
pos_top = row_found.loc[0,'top']
pos_width = row_found.loc[0,'top']
pos_height = row_found.loc[0,'top']

center_x = pos_left + (pos_width/2)
center_y = pos_left + (pos_width/2)
pgu.click(pos_x,pos_y)

# Split the text into sentences
sentences = text.split('. ')  # Assuming sentences end with a period followed by a space

# Get the bounding boxes for each sentence
sentence_boxes = []
for sentence in sentences:
    sentence_image = image.copy()
    sentence_box = pytesseract.image_to_boxes(sentence_image, lang='eng', config='--psm 6')
    sentence_boxes.append(sentence_box)

# Print the bounding boxes for each sentence
for i, sentence_box in enumerate(sentence_boxes):
    print(f"Sentence {i+1} bounding box: {sentence_box}")


