def number(val) :
    count = 0
    for idx in range(100, val+1) :
        a,b,c = map(int,list(str(idx)))
        first = a-b
        second = b-c

        if first == second :
            count +=1

    return 99 + count
    
num = int(input())

if num <100 :
     print(num)
elif num < 1000 :
    print(number(num))
else :
    print(number(999))
