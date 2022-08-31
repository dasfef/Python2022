# 아래의 예시 문자열에서 '/'로 구분된 각각의 옵션을 표시하고, PZ 옵션의 값을 x,y,w,h로 구분하여 표기하기
# 단, 최종 출력물은 다음과 같이 표기할 것(옵션의 순서는 변화 가능)
# PS = 121
# PZ.x = 2
# PZ.y = 3
# PZ.w = 100
# PZ.h = 100
# FILE = C:\Users\user11\Documents\Python\test.py

s = '/PS:121/PZ:2,3,100,100/FILE=test.py'

def sep(a) :
    if a.find('.py') == -1 :
        return 'Retry'
    s1 = a.split('/')    
    return s1[1], s1[2], s1[3]

result = sep(s)
print(result)
    
    
