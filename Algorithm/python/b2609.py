import math

def prime_factors(num) :
    lst = []
    value = 2
    first_num = num
    while True :
        if num%value == 0 :
            lst.append(value)
            num /= value
            
            if num ==1 :
                break
            
        else :
            value +=1
            if value >= math.sqrt(num) and first_num == num:
                lst.append(num)
                break
            
    return lst

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
        
def lcm(num1, num2) :
    num1 = prime_factors(num1)
    num2 = prime_factors(num2)
    dic = {}
    for prime in num1 :
        dic[prime] = num1.count(prime)

    for prime in num2 :
        if prime not in dic :
            dic[prime] = num2.count(prime)
        elif (prime in dic) and num2.count(prime) > dic[prime] :
            dic[prime] = num2.count(prime)
            
    total = 1
    for idx in dic :
        total *= (idx ** dic[idx])

    return total
        
val1, val2 = map(int, input().split())
print(gcd(val1, val2))
print(lcm(val1, val2))





        
