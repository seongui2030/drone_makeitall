from jikko.KiwiDrone import *
import keyboard
import time

drone = Kiwi_Serial("COM3")

drone.cmd_calibration()
time.sleep(10)
drone.cmd_arm()

print("숫자 1 키를 누르면 드론이 사각형 패턴으로 비행합니다.")

while True:
    if keyboard.is_pressed('1'):
        print("사각형 패턴 비행 시작!")

        drone.cmd_take_off()
        time.sleep(3)

        for i in range(4):
            drone.cmd_go(20) 
            time.sleep(3)
            drone.cmd_cw(90) 
            time.sleep(3)
            
        drone.cmd_landing()
        time.sleep(2)
        drone.cmd_disarm()
        print("사각형 패턴 비행 완료!")
        break

    time.sleep(1)