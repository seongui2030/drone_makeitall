from jikko.KiwiDrone import *
import keyboard

drone = Kiwi_Serial("COM3")

while(True):
 
    if keyboard.is_pressed('q'):
        drone.cmd_calibration()
    elif keyboard.is_pressed('w'):
        drone.cmd_arm()
    elif keyboard.is_pressed('e'):
        drone.cmd_take_off()
    elif keyboard.is_pressed('r'):
        drone.cmd_landing()