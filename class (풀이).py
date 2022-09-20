# Student class
# Person / Score class
# Inheritance test

class Person :
    #name = ""
    #age = -1
    #phone = ""

    def __init__(self, n, a, p) :
        self.name = n
        self.age = a
        self.phone = p

class Score :
    kor = -1
    eng = -1
    mat = -1

    def __init__(self, k=-1, e=-1, m=-1) :
        kor = k
        eng = e
        mat = m
        
    def tot(self) :
        return(kor + eng + mat)
        
    def ave(self) :
        return(tot() / 3)
    

class Student(Person) :
    hakbun = ""
    score = Score()
    
def PrintOut(sList) :                               # sList Student 객체의 리스트
    for i in range(len(sList)) :                    # sList의 인덱스 번호를 가져와서 다시 l의 []번째 인덱스 출력하는 방식
        print(f"{'%10s'%sList[i].name[0:10]}", end = "  ")
        print(f"{'%10s'%sList[i].hakbun[0:10]}", end = "  ")
        print(f"{'%10s'%sList[i].age}", end = "  ")
        print(f"{'%10s'%sList[i].phone[0:10]}")

def PrintOutEx(sList) :                               
    for i in sList :                    
        print(f"{'%10s'%i.name[0:10]}", end = "  ")
        print(f"{'%10s'%i.hakbun[0:10]}", end = "  ")
        print(f"{'%10s'%i.age}", end = "  ")
        print(f"{'%10s'%i.phone[0:10]}")

def sFromFile(fn, sList) :          # 파일 fn에서 읽어 Student 객체 리스트에 저장
    f = open(fn, 'r')
    for l in f :
        n = l.split(',')[0]
        a = int(l.split(',')[1])
        p = l.split(',')[2]
        x = Student(n, a, p)
        x.hakbun = l.split(',')[3]
        x.score.kor = int(l.split(',')[4])
        x.score.eng = int(l.split(',')[5])
        x.score.mat = int(l.split(',')[6])
        sList.append(x)
    
l = list()
ly = []
sFromFile("C:/Users/user11/Desktop/test.csv", ly)

##for i in f :
##    sp = i.split(',')
##    n = sp[0]
##    a = sp[1]
##    p = sp[2]
##    h = sp[3]
###while True :
##    #n = input("이름 : ")
##    #if (n == "") : break
##    #while True :
##    #    try :
##    #        a = int(input("나이 : "))
##    #        break
##    #    except :
##    #        print("나이란에는 숫자만 입력 가능합니다")
##    #        continue
##    
##    #p = input("전번 : ")
##    #h = input("학번 : ")
##    x = Person(n, a, p)
##    l.append(x)
##    y = Student(n, a, p)
##    y.hakbun = h
##    ly.append(y)


PrintOut(ly)
PrintOutEx(ly)


#print(f"x.name : {x.name}")
#print(f"x.age : {x.age}")
#print(f"x.phone : {x.phone}")
#print(l)
#print(len(l))
#print(f"y.name : {y.name}")
#print(f"y.age : {y.age}")
#print(f"y.phone : {y.phone}")
#print(f"y.hakbun : {y.hakbun}")
#print(len(ly))
