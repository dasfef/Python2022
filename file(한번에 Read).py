f = open("C:\\Users\\user11\\Documents\\Python\\sample.txt")    # file "sample.txt"를 읽기 전용 모드로 open. 단, text mode default.
full = f.read()
spread = full.split("\n")
i = 1

for ln in spread :
    print(f"{'%2d'%i} : {ln}\n", end='')
    i = i + 1

    c = ord(ln[0])
    print(f"{'%02x'%c}")
    

def txt(s) :
    sp = s.split("\n")
    i = 1
    for ln in sp :
        print(f"{'%3d'%i} : {ln}")
        i += 1
        
txt(full)
    



#for ln in f :                                                   # f를 문자열 리스트처럼 사용하여 한 라인씩 Read
#    print(f"{i} : {ln}", end='')
#    i += 1
