import keyboard
import time

print('키보드를 눌러봅시다!')

while(True):
    print(keyboard.read_key())
    time.sleep(1)