def test(st) :
    n = min(st)
    m = max(st)
    return n,m

def Main() :
    s = [1,7,3,9,5]
    #(x,y) = test(s)
    x = test(s)
    #print(f"Min = {x}, Max = {y}")
    print(f"{x}")

Main()
