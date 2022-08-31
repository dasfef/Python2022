# 보간문자열

x = 1
y = 2
print('X + Y =', x+y)  # x + y 출력
print('X =', x, 'Y =', y, '\nX + Y =', x+y)  # x, y 값을 나타낸 후 x + y 값 출력
print(f'X = {x}, Y = {y}, X + Y = {x+y}')  # f(보간문자열)을 활용하여 조금 더 직관적으로 표현


s = f'X = {x}, Y = {y}, X + Y = {x+y}'  # f(보간문자열) 만을 활용해도 똑같은 값 출력 가
print(s)


s = f'X = {x}, Y = {y}, X + Y = {x+y}, str = {"test"}'  # test 글귀와 같이 새로이 추가되는 내용이 있으면 기존 f의 따옴표와 다르게 구분지어 주어야 한다
print(s)
