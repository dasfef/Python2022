class Student :
    i = 0
    name = ""
    
    def Person(self) :
        self.i = self.i + 1
        print("학번 : ", self.i)
        
    def Person2(self, num, name, score) :
        self.num = num
        self.name = name
        self.score = score
        print("학번 : ", num, "이름 : ", name, "성적 : ", score)

    

    def Score(self, eng, math, kor) :
        self.eng = eng
        self.math = math
        self.kor = kor
        
              
an = Student()
bn = an.Person()
cn = an.Score()


        
