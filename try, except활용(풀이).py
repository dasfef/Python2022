# kbd에서 문자열을 입력 받아 숫자로 변환하는 프로그램 생성
# 단, 변환 오류시 경고 메시지를 출력하고 다시 입력

while True :
    s = input("숫자를 입력하세요 :")
    try :
        i = int(s)
        print(i)
    except :
        try :
            i = float(s)
            print(i)
        except :
            print("똑바로 입력하세요")
