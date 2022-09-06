# 최종 기대 출력물 : dic = {"길동": 1, "길순": 2, "길영": 2, "길민": 1}

ddd = {} #dict()
lst = ["길동", "길순", "길영", "길민", "길순", "길영"]

for n in lst :
    ddd[n] = ddd.get(n, 0) +1

print(ddd)    
