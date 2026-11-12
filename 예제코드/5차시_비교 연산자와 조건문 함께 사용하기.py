# 시험점수 0~100 사이의 값으로 입력
test = input("국어 시험 점수 : ")
test = int(test)

if test >=80 :
    print("A")
elif 60 <= test < 80 : 
    print("B")
elif 40 <= test < 60 :
    print("C")
else : 
    print("재시험을 응시하세요")