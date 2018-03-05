#--시간초과--
import sys

num, ans = map(int, input().split())
lst = [0] + list(map(int, sys.stdin.readline().split()))
interval = list(map(lambda x : x.strip(), sys.stdin.readlines()))

for idx in interval :
    s, f = map(int, idx.split())
    sys.stdout.write(str(sum(lst[s:f+1])) + "\n")


#--DP--
import sys

num, ans = map(int, input().split())
lst = [0] + list(map(int, sys.stdin.readline().split()))
interval = list(map(lambda x : x.strip(), sys.stdin.readlines()))
sum_lst = [False] * (num+1)

total = 0
for idx, n in enumerate(lst) :
    total += n
    sum_lst[idx] = total

for idx in interval :
    s, f = map(int, idx.split())
    sys.stdout.write(str(sum_lst[f] - sum_lst[s-1]) + "\n")
        
