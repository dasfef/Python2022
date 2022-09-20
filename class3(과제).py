class Score :

    def __init__(self, n, k, e, m) :
        self.name = n
        self.kor = k
        self.eng = e
        self.mat = m

def FF(fn, sList) :
    f = open(fn, 'r')
    for j in f :
        a = j.split(',')
        n = a[0]
        k = a[1]
        e = a[2]
        m = a[3]
        x = Score(n, k, e, m)
        sList.append(x)

def PrintOut(sList) :
    for i in sList :
        print(f"{'%10s'%i.name}", end = ' ')
        print(f"{'%10s'%i.kor}", end = ' ')
        print(f"{'%10s'%i.eng}", end = ' ')
        print(f"{'%10s'%i.mat}", end= ' ')

def kAverage(sList) :
    for i in sList :
        i = i + 1
        x = int(i.kor) + i
        print(x)
        

li = list()
FF("C:/Users/user11/Desktop/score.csv", li)
PrintOut(li)              
kAverage(li)
