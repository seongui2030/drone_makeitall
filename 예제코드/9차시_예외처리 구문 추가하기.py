import speech_recognition as sr

# 음성 인식 객체 생성
recognizer = sr.Recognizer()

# 마이크에서 입력받기
with sr.Microphone() as source:
    try :
        print("마이크를 통해 음성을 인식시키세요!...")
        audio = recognizer.listen(source, 5)
        
        # Google Speech Recognition API를 사용하여 음성 인식
        print("인식된 텍스트 : " + recognizer.recognize_google(audio, language='ko-KR'))
    except sr.UnknownValueError:
        print("Google Speech Recognition API가 당신의 말을 이해하지 못했습니다.")
    except sr.WaitTimeoutError : 
        print("마이크에 음성이 입력되지 않았습니다! 음성을 입력해주세요!")
    except sr.RequestError as e : 
        print(f"Google Speech Recognition API 서비스에 문제가 발생했습니다; {e}")
        
