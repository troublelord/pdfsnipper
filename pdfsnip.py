#from pynput.keyboard import Key, Controller
import time
#from directkeys import PressKey, ReleaseKey, UP, DOWN, RIGHT
import keyboard
import numpy as np 
import cv2 
import pyautogui 

######################
#images will be saved as image + count + .png

count=1

##########################
#total page number here

pgno=40

#########################
#time before snip begins

time.sleep(5)
   
###################################
#image size here
  
x1=571
x2=1327
y1=5
y2=1074

####################################
x=x1
y=y1
h=y2-y1
w=x2-x1


#keyboard = Controller()
#key = Key.page_down





try:
	while(count<pgno):
		image = pyautogui.screenshot()
		image = cv2.cvtColor(np.array(image), 
                     cv2.COLOR_RGB2BGR) 
		image = image[y:y+h, x:x+w]
 
		cv2.imwrite(str(count)+".png", image)
		
		time.sleep(0.5)
		
		print(count)
		keyboard.press_and_release('right')
		 
   

		 
		count=count+1
		time.sleep(0.5)

except KeyboardInterrupt:
	pass