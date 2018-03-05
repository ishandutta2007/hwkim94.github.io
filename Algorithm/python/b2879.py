import sys

def calculate(lst) :
    result = 0
    last = 0
    lst = list(map(abs, lst))

    for idx in lst :
        value = idx - last
        if value <= 0 :
            value = 0
        
        result += value
        last = idx
        
    return result

n = int(input())
incor = list(map(int, sys.stdin.readline().split()))
cor = list(map(int, sys.stdin.readline().split()))

total = 0
lst = [idx - idx2 for idx, idx2 in zip(incor, cor)]
temp = []
for idx in lst :
    if idx == 0 :
        total += calculate(temp)
        temp = []
        continue

    if not temp :
        temp.append(idx)
        continue

    if idx * temp[-1] > 0 :
        temp.append(idx)
        
    else :
        total += calculate(temp)
        temp = [idx]
        
if temp :
    total += calculate(temp)
print(total)
