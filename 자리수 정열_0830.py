# 자리수 정열

x = 1
y = 2

s = f'X = {x}, Y = {y}, X + Y = {x+y}, str = {"%10s"%"test"}'  # "%10s"% 를 붙여 자리수를 정열함
print(s)


s = f'X = {x}, Y = {y}, X + Y = {x+y}, str = {"[%10s]"%"test"}'  # [ ] 로 얼마나 공백을 만드는지 확인
print(s)


s = f'X = {"[%10d]"%x}, Y = {y}, X + Y = {x+y}, str = {"[%10s]"%"test"}'  # %d : 10진수 / %f : 소수표현 / %s : 문자열 / %c : 문자(단일문자)
print(s)                                                                  # %와 (d,f,s,c) 사이의 숫자로 자리수를 기입 
                                                                          # d = / f = float / s = string / c = character


x = 50
s = f'문자코드 value : {x} : 문자 : [{"%c"%x}]'  # ASCII 코드로 확인하기 (?)
print(s)
