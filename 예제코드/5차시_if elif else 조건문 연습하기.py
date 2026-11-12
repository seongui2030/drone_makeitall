weather = input("오늘의 날씨는? :")

if weather == '비' :
    print( "우산을 챙기세요!" )
elif weather == '눈' :
    print( "바닥이 미끄러우니 조심하세요." )
elif weather == '미세먼지' :
    print( "마스크를 챙기세요." )
else :
    print( "좋은 하루 되세요!" )
