# import libraries
import time 
import os 

def take_picture():
	os.system('sudo fswebcam -r 1280x720 -S 3 --jpeg 50 --save /home/pi/CSC3004/test_image.jpg') # uses Fswebcam to take picture
	time.sleep(2)
	print("Photo taken!") 
	# this line creates a 15 second delay before repeating the loop

take_picture()
