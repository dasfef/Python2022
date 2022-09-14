f = open("C:\\Users\\user11\\Documents\\Python\\sample.txt", mode = 'r')
i = 1

for ln in f :
    print(f"{'%3d'%i} : {ln}", end = ' ')
    i = i + 1

    for s in ln :
        c = ord(s)       # 단일 문자(열) s의 아스키 코드 값 반환
        print(f"{'%02x'%c}", end = ' ')
    print()        
