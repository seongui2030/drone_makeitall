from jikko.KiwiDrone import *

drone = Kiwi_Serial("COM3")

drone.cmd_calibration()
time.sleep(10)

drone.cmd_arm()

drone.cmd_take_off()
time.sleep(3)

drone.cmd_go(10)
time.sleep(2)

drone.cmd_back(10)
time.sleep(2)

drone.cmd_left(10)
time.sleep(2)

drone.cmd_right(10)
time.sleep(2)

time.sleep(3)

drone.cmd_landing()
time.sleep(1)

drone.cmd_disarm()
