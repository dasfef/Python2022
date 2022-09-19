class Person :
    name = ""
    age = -1
    phone = ""

    def __init__(self, n, a, p) :
        self.name = n
        self.age = a
        self.phone = p

while True :
    n = input("이름 : ")
    a = input("나이 : ")
    p = input("전번 : ")
