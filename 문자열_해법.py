def func(s) :
    str = s.split(' ')
    print(str)
    ret = ''
    for s1 in str :
        ss1 = s1.lower()
        ss2 = ss1[0].upper() + ss1[1:]
        ret = ret + ' ' + ss2
    return ret

x = input('영어 문장을 입력하세요 :')
y = func(x)
print(x, ' ==>', y)
