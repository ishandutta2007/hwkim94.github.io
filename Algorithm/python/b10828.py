c= int(input())
lst = []
for idx in range(c):
    a = input().split()
    if len(a) == 2 :
        val1, val2 = a
    else:
        val1 = a[0]
    
    if val1 == "push":
        lst.append(int(val2))
        
    elif val1 == "pop":
        if len(lst) != 0 :
            print(lst[-1])
            del lst[-1]
        else :
            print(-1)
            
    elif val1 == "size":
        print(len(lst))
        
    elif val1 == "empty" :
        if len(lst) != 0:
            print(0)
        else :
            print(1)
            
    elif val1 == "top":
        if len(lst) != 0 :
            print(lst[-1])
        else :
            print(-1)
