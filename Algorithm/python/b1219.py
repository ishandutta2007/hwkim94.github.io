#같은 경로로 가는 입력이 주어지고 다른 비용이 드는 입력이 주어질 경우가 존재
#따라서 인접행렬보다 인접리스트가 좋음

import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

#--input--
city, start, end, path = map(int, input().split())

inverse_path = defaultdict(lambda : [])
cost_dic = defaultdict(lambda : [])
for idx in range(path) :
    s, e, c = map(int, input().split())
    cost_dic[s].append((e,c))
    inverse_path[e].append(s)
    
money = list(map(int, input().split()))

#--declaration--
INF = float("inf")
can_go_end_lst = [False] * city

def dfs(ver) :
    can_go_end_lst[ver] = True
    
    for idx in inverse_path[ver] :
        if not can_go_end_lst[idx] :
            dfs(idx)
    
def bellman_ford(start, end) :
    dfs(end)
    result = defaultdict(lambda : -INF)
    result[start] = money[start]
    flag = False

    for num in range(city) :
        for s, idx in cost_dic.items() :
            for e, cost in idx :
               
                if result[s] - cost + money[e] > result[e] :
                    result[e] = result[s] - cost + money[e]
                    
                    if (num == city-1) and can_go_end_lst[e] :
                        flag = True
                        break

    if result[end] == -INF :
        return "gg"
    
    else :
        if flag :
            return "Gee"

        else :
            return result[end]
        
#--main--
print(bellman_ford(start, end))
