from jikko.KiwiDrone import *
import keyboard
import time

# 드론 연결
drone = Kiwi_Serial("COM3")

# 캘리브레이션 및 이륙 준비
drone.cmd_calibration()
time.sleep(10)
drone.cmd_arm()

print("숫자 2 키를 누르면 드론이 삼각형 패턴으로 비행합니다.")

while True:
    if keyboard.is_pressed('2'):
        print("삼각형 패턴 비행 시작!")

        drone.cmd_take_off()
        time.sleep(3)

        for i in range(3):
            drone.cmd_go(20)      
            time.sleep(3)
            drone.cmd_cw(120)     # 120도 시계방향 회전
            time.sleep(3)

        drone.cmd_landing()
        time.sleep(2)
        drone.cmd_disarm()
        print("삼각형 패턴 비행 완료!")
        break

    time.sleep(1) 
