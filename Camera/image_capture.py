# import libraries
import time 
import os 

def take_picture():
	os.system('fswebcam -r 1280x720 -S 3 --jpeg 50 --save test_image.jpg') # uses Fswebcam to take picture
	time.sleep(2)
	print("Photo taken!") 
