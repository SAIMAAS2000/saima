from gpiozero import MotionSensor
import os
pir = MotionSensor(4)
if(pir.motion_detected):
    os.system("fswebcam -F 5 --fps 20 -r 1200x800 33.jpg")
    print("Motion detected!")
    print("pic taken")
    
    
