#-----풀이1----
import sys

num = int(input())
lst = sorted(list(map(int,list(map(lambda x : x.strip(), sys.stdin.readlines())))), reverse = True)
max_w = 0

while lst :
    temp = num * lst.pop()

    if max_w < temp :
        max_w =temp
    num -= 1
    
print(max_w)


#-----풀이2----
import sys

num = int(input())
lst = sorted(list(map(int,list(map(lambda x : x.strip(), sys.stdin.readlines())))))
max_w = 0

for idx in range(num) :
    temp = lst[idx] * (num-idx)

    if temp > max_w :
        max_w = temp

print(max_w)
