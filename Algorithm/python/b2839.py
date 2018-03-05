#----1번째 풀이----
import sys
sys.setrecursionlimit(100000)

num = int(input())
dic = {0 : 0, 1 : float("inf"), 2 : float("inf"), 3 : 1, 4 : float("inf"),5 :1}

def sugar(val) :
    if val in dic :
        return dic[val]

    else :
        temp = min(sugar(val-3), sugar(val-5)) + 1
        dic[val] = temp
        
        return temp

result = sugar(num)

if result ==float("inf") :
    print(-1)
else :
    print(result)


#----2번째 풀이----
num = int(input())

def sugar2(val) :
    five = val//5
    remainder = val%5
    three = remainder//3
    remainder =remainder%3
    
    while remainder and five > 0 :
        five -= 1
        remainder +=5
        three += remainder//3
        remainder = remainder%3
        
    if remainder != 0 :
        return -1
    else :
        return five + three

print(sugar2(num))


#----3번째 풀이(가장 효율적)----
n=int(input())
three=0
five=n//5
n%=5

while five>=0:
    if n%3==0:
        three=n//3
        n%=3
        break
    
    five-=1
    n+=5


if n==0 :
    print(five+three)
else :
    print(-1)
