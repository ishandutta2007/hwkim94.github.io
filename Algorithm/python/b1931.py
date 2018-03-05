import sys
from operator import itemgetter

num = int(input())
data = sorted(list(map(lambda x: tuple(map(int, x.strip().split())),sys.stdin.readlines())))
data.sort(key = itemgetter(1))

last = 0
count = 0

for start, finish in data :
    if last <= start :
        count+=1
        last = finish

print(count)
