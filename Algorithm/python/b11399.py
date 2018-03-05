#----1번째----
import sys

num = int(input())
lst = sorted(list(map(int, sys.stdin.readline().split())))
total = result = 0
for idx in lst : total += idx; result += total
    
print(result)

#----2번째----
import sys

num = int(input())
lst = sorted(list(map(int, sys.stdin.readline().split())))
result = 0
for idx, val in enumerate(lst) : result += val * (num-idx)

print(result)
