def gcd(num1, num2) :
    b = max(num1, num2)
    a = min(num1, num2)
    r = b%a
    flag = True
    if r == 0 :
        flag = False
    
    while flag :
        b = a
        a = r
        r = b%a

        if r == 0 :
            break

    return a
        
val1, val2 = map(int, input().split())
print("1" * gcd(val1, val2))


        
