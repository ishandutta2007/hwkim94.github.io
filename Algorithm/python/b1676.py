import math
n = int(input())
num =math.factorial(n)
count = 0

if n <5 :
    print(0)
else :
    while True :
        num //= 10
        count += 1
        
        if num%10 != 0 :
            print(count)
            break

