Dict = dict()
#Read = open("sentence.txt")

#for x in Read :
#    p = print({x})

def Make(s) :
    for i in s :
        Dict[i] = Dict.get(i, 0) + 1
    

def Sep(j) :
    String = str(j)
    for jj in String :
        spl = jj.split(" ")
        Make(spl)
    #print(Dict)
            

def Main() :
    Read = open("sentence.txt")
    for x in Read :
        x1 = print({x})
        xSplit = x.split(" ")
        Make(xSplit)
        #p = print({x})
        #Sep(p)
    print(Dict)


def Main3() :
    Read = open("sample.txt")
    for x in Read :
        x1 = x.strip()
        print(x1)

    
Main3()        
        

        
