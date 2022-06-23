# import libraries
import time 
import os 

def run_human_detection():
    filename='test_image3.jpg'
    command_string = 'python human_detection.py -i '+filename
    os.system(command_string)
    time.sleep(2)
    print("Running detection on photo!")
    
run_human_detection()
