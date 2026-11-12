from jikko.KiwiDrone import *
import keyboard

drone = Kiwi_Serial("COM3")

while(True):
    
    if keyboard.is_pressed('z'):
        drone.cmd_calibration()
        time.sleep(10)
    elif keyboard.is_pressed('x'):
        drone.cmd_arm()
    elif keyboard.is_pressed('c'):
        drone.cmd_take_off()
    elif keyboard.is_pressed('v'):
        drone.cmd_landing()
    elif keyboard.is_pressed('b'):
        drone.cmd_disarm()
    elif keyboard.is_pressed('ESC'):
        drone.cmd_landing()
        time.sleep(1)
        drone.cmd_disarm()
        break
    
    if keyboard.is_pressed('up'):
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
        
    if keyboard.is_pressed('w'):
        drone.cmd_up(20)
        time.sleep(2)
    elif keyboard.is_pressed('s'):
        drone.cmd_down(20)
        time.sleep(2)
    elif keyboard.is_pressed('a'):
        drone.cmd_ccw(90)
        time.sleep(3)
    elif keyboard.is_pressed('d'):
        drone.cmd_cw(90)
        time.sleep(3)
        