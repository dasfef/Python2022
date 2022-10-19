range(1, 10)

s = range(30, 80)   # range 함수는 리스트로 변수에 들어간다
list(s)

list(range(30, 120))

bytes(range(30, 120))
bytes(range(65, 91))    # 영어 알파벳 A ~ Z 까지의 범위를 bytes 함수를 이용해 나타낸다

chr(65)     # chr 함수를 이용해 특정 위치에 있는 리스트를 반환

int.from_bytes(b'X')        # 오류발생
a = int.from_bytes(b'X', 'big')     # int 클래스의 메소드(from_bytes)를 통해 우리가 원하는 문자의 코드값을 알 수 있다 * endian 값을 big, little 중 골라주어야 한다
a = int.from_bytes(b'X', 'little')      # big, little endian의 값이 달라도 반환하는 값은 똑같다
a = int.from_bytes(b'가', 'big')    # 한글일 경우 syntax 오류 발생(* 0 ~ 127 까지의 아스키 코드 문자로 표기가 되는데, 한글은 아스키 코드에 포함이 되지 않기 때문)



# 어떤 문자의 코드값을 알아내기란 번거로운 작업이지만, 생각보다 쉬운 방법이 존재한다


s = bytes(range(65, 91))    # A ~ Z 

a = s[2]    # C 라는 값이 반환된다
b = int.from_bytes(bytes(a), 'big')     # typeerror 오류 발생(encoding 에러)
b = int.from_bytes(bytes(a, 'UTF-8', 'big'))    # UTF-8 과 같은 유형의 encoding argument를 추가해주어야 한다

bytes(a, 'UTF-8')[0]    # 위의 b 값과 동일하게 나오는 것을 볼 수 있다 / str 타입에는 꼭 encoding type이 추가되어야 한다(숫자는 관계 없음)
bytes('a', 'UTF-8')[0]      # 문자열의 경우 ''로 구분하여 나타내준다


# Hexa 변환식
s = 'abcd'
s.encode

b = s.encode('ANSI')
print(f"{'%02'%b[1]}")


#########  ★ 16진수 표기 및 정렬 ★  #########

s = bytes(range(65, 91))
b = bytearray(s, 'UTF-8')
b   # bytearray(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

f"{'%02X'%b[1]}"    # format 구문에서 %02X 처럼 x를 대문자로 써준다면 표기되는 알파벳 값도 대문자로 표기된다

for a in b :
    print(f"{'%02X'%a}", end = ' ')     # a값, 즉 bytearray 시킨 s를 출력하면 한줄로 2칸씩 나누어 출력한다

for i in range(len(b)) :        # 위의 for 문과 결과는 동일하지만 index 값으로 주는 것이 분별을 명확히 할 수 있다
    if (i % 16 == 0) :
        print(f"{'%08X'%i} : ", end = ' ')      # 포맷문자열 안에서의 콜론(:)의 의미 : 인덱스 앞 ~ 뒤
    print(f"{'%02X'%b[i]}", end = ' ')      
    if((i + 1) % 8 == 0) :
        if((i + 1) % 16 == 0) :
            print("")
        else : print("| ", end = ' ')


