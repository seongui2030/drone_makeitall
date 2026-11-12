import keyboard
import time

def num2(event) :
    print(f"{event.name}키가 입력되었습니다.")

while(True):

    keyboard.on_press_key('2', num2, True)
    time.sleep(1)
