from jikko.KiwiDrone import *
import speech_recognition as sr
import time

drone = Kiwi_Serial("COM3")   # 시리얼 포트는 환경에 맞게 설정
drone.cmd_calibration()
time.sleep(10)
drone.cmd_arm()
print("음성 명령 '원형 비행'을 인식하면 드론이 원형 패턴으로 비행합니다.")

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("음성 명령을 말씀하세요...")
        audio = recognizer.listen(source, 5)
        try:
            text = recognizer.recognize_google(audio, language='ko-KR')
            print("인식된 텍스트 :", text)

            if "원형 비행" in text:
                print("원형 비행 명령 인식! 드론이 원형 패턴으로 비행합니다.")
                drone.cmd_take_off()
                time.sleep(3)

                for i in range(36):
                    drone.cmd_go(10)
                    time.sleep(1)
                    drone.cmd_cw(10)
                    time.sleep(1)
                drone.cmd_landing()
                time.sleep(1)
                drone.cmd_disarm()
                print("원형 패턴 비행 완료!")
                break

        except sr.UnknownValueError:
            print("음성을 인식하지 못했습니다.")
        except sr.RequestError as e:
            print(f"음성 인식 서비스 오류: {e}")

    time.sleep(2)
