# 아래의 예시 문자열에서 '/'로 구분된 각각의 옵션을 표시하고, PZ 옵션의 값을 x,y,w,h로 구분하여 표기하기
# 단, 최종 출력물은 다음과 같이 표기할 것(옵션의 순서는 변화 가능)
# PS = 121
# PZ.x = 2
# PZ.y = 3
# PZ.w = 100
# PZ.h = 100
# FILE = C:\Users\user11\Documents\Python\test.py

s = '/PS:121 /PZ:2,3,100,100 /FILE=C:\\test.py'
s2 = '/PZ:2,3,100,100 /PS:121 /FILE=C:\\test.py'
s3 = '/FILE=C:\\test.py /PS:121 /PZ:2,3,100,100'

def get_PS(s) :             # /PS 옵션을 인수로 받아 옵션의 값을 리턴, s = /PS:121
    x = s.split(':')
    return (x[1])

def get_PZ(s) :             # /PZ 옵션을 인수로 받아 옵션의 값을
    x = s.split(':')        # x,y,w,h 리스트로 리턴, s = /PZ:2,3,100,100
    y = x[1].split(',')     # y = ['2', '3', '100', '100']
    return (y)              # y의 값은 리스트(배열) 값
