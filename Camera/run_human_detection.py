# import libraries
import time 
import os 

def run_human_detection():
	os.system("python human_detection.py -i 'test_image.jpg'") # uses Fswebcam to take picture
	time.sleep(2)
	print("Running detection on photo!") 
	

run_human_detection()