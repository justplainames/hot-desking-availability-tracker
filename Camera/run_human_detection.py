# import libraries
import time 
import os 
from io import StringIO
import sys
import image_capture



def run_human_detection():
    image_capture.take_picture()
    time.sleep(2)
    filename='test_image.jpg'
    command_string = 'python human_detection.py -i '+filename
    os.system(command_string)
    time.sleep(2)
    
while(True):
    run_human_detection()
    time.sleep(30)
