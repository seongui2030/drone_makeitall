import speech_recognition as sr

# 음성 인식 객체 생성
recognizer = sr.Recognizer()

# 마이크에서 입력받기
with sr.Microphone() as source:
    print("마이크를 통해 음성을 인식시키세요!...")
    audio = recognizer.listen(source, 5)

    print("인식된 텍스트 : " + recognizer.recognize_google(audio, language='ko-KR'))
