def blank(s) :
    q = {}
    for i in s :
        q[i] = q.get(i, 0) +1
        print(q)

def Main() :
    inp = input("문장을 입력하세요 : ")
    sep = inp.split(" ")
    sep_2 = str(sep)
    blank(sep_2)


Main()
