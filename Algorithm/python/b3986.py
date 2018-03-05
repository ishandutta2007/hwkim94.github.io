import sys

def good(line) :
    lst = [line[0]]
    
    for idx in line[1:] :
        if not lst :
            lst.append(idx)
            
        else :
            if idx != lst[-1] :
                lst.append(idx)
            else :
                lst.pop()

    if not lst :
        return True
    else :
        return False
        
num = int(input())
lines = list(map(lambda x : x.strip(), sys.stdin.readlines()))

result = 0
for line in lines :
    if good(line) :
        result += 1

print(result)

#다른 풀이
#위의 풀이는 리스트의 크기로 추정되는 문제때문에 런타임 에러 발생
import sys

def good(line) :
    lst = [line[0]]
    
    for idx in line[1:] :
        if not lst :
            lst.append(idx)
            
        else :
            if idx != lst[-1] :
                lst.append(idx)
            else :
                lst.pop()
    
    if not lst :
        return True
    else :
        return False

num = int(input())
result = 0 
for idx in range(num) :
    line = sys.stdin.readline().strip()
    if good(line) :
        result += 1

print(result)
        

