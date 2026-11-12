from jikko.KiwiDrone import *

drone = Kiwi_Serial("COM3")

drone.cmd_calibration()
time.sleep(10)

drone.cmd_arm()

drone.cmd_take_off()
time.sleep(3)

drone.cmd_down(20)
time.sleep(2)
drone.cmd_cw(180)
time.sleep(5)

drone.cmd_ccw(90)
time.sleep(2)

time.sleep(3)

drone.cmd_landing()
time.sleep(1)

drone.cmd_disarm()
