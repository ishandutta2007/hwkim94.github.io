#실패코드
#두 개의 line이 있다고 생각하고, 큰 순서대로 번갈아가며 그 line을 채움
#그러면 각각 채워질 것이고, 정답이 반드시 있다고 하였으므로 반드시 채워지게 됨
import sys

t,n = map(int, input().split())
r = list(map(int, sys.stdin.readline().split()))

member = []
for idx, time in enumerate(r) :
    member.append((idx, time))

member = sorted(member, key=lambda x : x[1], reverse = True)
start = [False] * n
line1 = []
line2 = []
time1 = 0
time2 = 0

for idx in member :
    num = idx[0]
    time = idx[1]
    
    if time1 < time2 :
        line1.append(num)
        start[num] = time1
        time1 += time
    else :
        line2.append(num)
        start[num] = time2
        time2 += time

print(" ".join(list(map(str, start))))

#--------------------------------------------
#냅색 알고리즘
#http://blog.daum.net/rhaoslikesan/287

import sys
sys.setrecursionlimit(1000000)

t,n = map(int, input().split())
r = list(map(int, sys.stdin.readline().split()))
time = [False] + r 

dic = {}
def recursion(n, t) :
    if (n,t) in dic :
        return dic[(n,t)]

    else :
        temp_time = time[n]

        if t >= temp_time:
            temp1, temp2 = False, False

            #다음에 진행될 recursion에 0이 있는 경우
            if n-1 == 0 :
                dic[(0,t)] = 0
                dic[(0,t-temp_time)] = 0
                
            if t == temp_time :
                dic[(n-1, 0)] = 0

            #n이 포함되지 않을 경우                
            if (n-1, t) in dic :
                temp1 = dic[(n-1, t)]
            else :
                temp1 = recursion(n-1, t)

            #n이 포함될 경우
            if (n-1, t-temp_time) in dic :
                temp2 = dic[(n-1, t-temp_time)] + temp_time
            else :
                temp2 = recursion(n-1, t-temp_time) + temp_time
                
            val = max(temp1, temp2)
            dic[(n,t)] = val
            return val

        else :
            if (n-1, t) in dic :
                val = dic[(n-1,t)]
                dic[(n, t)] = val
                return val
            
            else :
                if n-1 == 0 :
                    dic[(0, t)] = 0
                    return 0
                else :
                    val = recursion(n-1, t)
                    dic[(n, t)] = val
                    return val

def findElement(n, t, v) :
    lst = []

    for idx in range(n, 1, -1):
        
        if dic[(idx,t)] != dic[(idx-1,t)] :
            lst.append(idx)
            val = time[idx]
            v = v - val
            t = t - val
            
            if v == 0 :
                break
            
        if idx == 2 :
            lst.append(idx-1)
            break

    return lst
        
#----main            
recursion(n, t)
value = max(dic.items(), key = lambda x : x[1])
lst1 = findElement(n,t, value[1])
lst2 = [idx for idx in range(1, n+1) if idx not in lst1]

total1, total2 = 0,0
tot = []
for seq in range(1, n+1) :
    val = time[seq]
    
    if seq in lst1 :
        tot.append(total1)
        total1 += val
        
    else :
        tot.append(total2)
        total2 += val

print(" ".join(list(map(str, tot))))
