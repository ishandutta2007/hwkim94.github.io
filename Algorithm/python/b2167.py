import sys

a,b = map(int, input().split())
dic = {}

for idx in range(a) :
    lst = list(map(int, sys.stdin.readline().split()))
    dic[idx] = lst


num = int(input())
cmd = list(map(lambda x : x.strip(), sys.stdin.readlines()))

for idx in cmd :
    x1,y1,x2,y2  = map(int, idx.split())
    print(sum([sum(dic[x1+idx-1][y1-1:y2]) for idx in range(x2-x1+1)]))
