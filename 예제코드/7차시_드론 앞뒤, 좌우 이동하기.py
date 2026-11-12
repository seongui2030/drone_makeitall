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

    elif keyboard.is_pressed('up'):
        drone.cmd_go(10)
        time.sleep(2)
    elif keyboard.is_pressed('down'):
        drone.cmd_back(10)
        time.sleep(2)
    elif keyboard.is_pressed('left'):
        drone.cmd_left(10)
        time.sleep(2)
    elif keyboard.is_pressed('right'):
        drone.cmd_right(10)
        time.sleep(2)
