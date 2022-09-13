while True :
    kbd = input('숫자를 입력하세요 : ')
    try :
        kbdo = int(kbd)
        print(kbdo)
    except :
        kbdx = 'retry'
        print(kbdx)
        
