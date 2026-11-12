from jikko.KiwiDrone import *
import speech_recognition as sr

drone = Kiwi_Serial( "COM3" )

# 음성 인식 객체 생성
recognizer = sr.Recognizer()

while True :
    # 마이크에서 입력받기
    with sr.Microphone() as source:
        try:
            print("마이크를 통해 음성을 인식시키세요!...")
            audio = recognizer.listen(source, 5)
            
            # Google Speech Recognition API를 사용하여 음성 인식
            text = recognizer.recognize_google(audio, language='ko-KR')
            print("인식된 텍스트 : " + text)

            # 변환된 텍스트를 기반으로 드론 동작
            if (text == '센서 보정') :
                drone.cmd_calibration()
                time.sleep(10)
            elif (text == '시동 켜'):
                drone.cmd_arm()
            elif (text == '이륙'):
                drone.cmd_take_off()
            elif (text == '착륙'):
                drone.cmd_landing()
            elif (text == '시동 꺼'):
                drone.cmd_disarm()
            elif (text == '종료'):
                drone.cmd_landing()        
                time.sleep(1)
                drone.cmd_disarm()
                break

            if (text == '전진'):
                drone.cmd_go(10)
                time.sleep(2)
            elif (text == '후진'):
                drone.cmd_back(10)
                time.sleep(2)
            elif (text == '왼쪽'):
                drone.cmd_left(10)
                time.sleep(2)
            elif (text == '오른쪽'):
                drone.cmd_right(10)
                time.sleep(2)

            if (text == '상승'):
                drone.cmd_up(20)
                time.sleep(2)
            elif (text == '하강'):
                drone.cmd_down(20)
                time.sleep(2)
            elif (text == '좌회전'):
                drone.cmd_ccw(90)
                time.sleep(3)
            elif (text == '우회전'):
                drone.cmd_cw(90)
                time.sleep(3)

        except sr.UnknownValueError:
            print("Google Speech Recognition API가 당신의 말을 이해하지 못했습니다.")
        except sr.WaitTimeoutError:
            print("마이크에 음성이 입력되지 않았습니다! 음성을 입력해주세요!")
        except sr.RequestError as e:
            print(f"Google Speech Recognition API 서비스에 문제가 발생했습니다; {e}")

    print("3초 후 음성인식이 다시 진행됩니다...")
    time.sleep(3)

