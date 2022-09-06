# while 문의 리스트 표현 활용 비교

#total = 0
#count = 0

#while True :
#    inp = input('숫자를 입력하세요 :')
#    if inp =="done" :
#        break
#    value = float(inp)
#    total = total + value
#    count = count + 1

#average = total / count
#print("평균 :", average)


numlist = list()

while True :
    inp = input("값을 입력하세요 : ")
    if inp == "done" : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("평균 :", average)



# 리스트로 표현할 시 장점 : 입력된 값의 히스토리를 알아볼 수 있다
# 위의 while 문과 동일한 값을 출력할 수 있지만 리스트로 표현시 장점을 알아볼 수 있다.
