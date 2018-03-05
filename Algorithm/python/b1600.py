#dfs방식 -> 시간초과 : 메모라이제이션을 해줘야함

import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

def makingGraph(row, col, lst_map) :
    dic = defaultdict(lambda : [])
    horse = []
    ub = row*col
    node = 0
    
    for elt in lst_map[1:] :
        node += 1
        
        if elt :     
            #상
            pos = node-col
            if pos > 0 :
                if lst_map[pos] :
                    dic[node].append(pos)
            #하
            pos = node+col
            if pos <= ub :
                if lst_map[pos] :
                    dic[node].append(pos)
            #좌
            pos = (node%col)-1
            if pos != 0 :
                if lst_map[node-1] :
                    dic[node].append(node-1)
            #우
            pos = (node%col)+1
            if pos != 1 :
                if lst_map[node+1] :
                    dic[node].append(node+1)
                    
            #1
            pos1 = node-col
            pos2 = (node%col)-2
            if pos1 > 0 and (pos2 not in (-1, 0)) :
                pos = pos1 - 2
                if lst_map[pos] :
                    dic[node].append(pos)
                    horse.append((node, pos))
            #2
            pos1 = node-col*2
            pos2 = (node%col)-1
            if pos1 > 0 and pos2 != 0 :
                pos = pos1 - 1
                if lst_map[pos] :
                    dic[node].append(pos)
                    horse.append((node, pos))
            #3
            pos1 = node-col*2
            pos2 = (node%col)+1
            if pos1 > 0 and pos2 != 1 :
                pos = pos1 +1
                if lst_map[pos] :
                    dic[node].append(pos)
                    horse.append((node, pos))
            #4
            pos1 = node-col
            pos2 = (node%col)+2
            if pos1 > 0 and (pos2 not in (col+1, 2)) :
                pos = pos1 +2
                if lst_map[pos] :
                    dic[node].append(pos)
                    horse.append((node, pos))
            #5
            pos1 = node+col
            pos2 = (node%col)+2
            if pos1 <= ub and (pos2 not in (col+1, 2)) :
                pos = pos1 +2
                if lst_map[pos] :
                    dic[node].append(pos)
                    horse.append((node, pos))
            #6
            pos1 = node+col*2
            pos2 = (node%col)+1
            if pos1 <= ub and pos2 != 1 :
                pos = pos1 +1
                if lst_map[pos] :
                    dic[node].append(pos)
                    horse.append((node, pos))
            #7
            pos1 = node+col*2
            pos2 = (node%col)-1
            if pos1 <= ub and pos2 != 0 :
                pos = pos1 -1
                if lst_map[pos] :
                    dic[node].append(pos)
                    horse.append((node, pos))
            #8
            pos1 = node+col
            pos2 = (node%col)-2
            if pos1 <= ub and (pos2 not in (-1, 0)) :
                pos = pos1 -2
                if lst_map[pos] :
                    dic[node].append(pos)
                    horse.append((node, pos))

    return dic, horse

def dfs(x, num, move, check) :
    check[x] = True
    result = []
    
    if x == goal :
        return [move]
        
    for y in graph[x] :
        
        if not check[y] :
            if (x, y) in horse :
                if num < K :
                    result.extend(dfs(y, num+1, move+1, list(check)))

            else :
                result.extend(dfs(y, num, move+1, list(check)))

    if not result :
        return [float('inf')]
    else :
        return [min(result)]

#----main----
K = int(input())
row, col = map(int, input().split())
i_map = list(map(lambda x : x.strip(), sys.stdin.readlines()))

lst_map = [False]
for r in i_map :
    lst_map.extend(list(map(lambda x : not bool(int(x)), r.split())))

goal = row*col
graph, horse = makingGraph(row, col, lst_map)
check = [False]*(goal+1)
result = dfs(1, 0, 0, list(check))

mini = result[0]
if mini == float("inf") :
    print(-1)
else :
    print(mini)

#---------------------------------------------------------
#bfs방식
    
import sys
import copy
from collections import defaultdict
sys.setrecursionlimit(1000000)

def checkingMatrix(x, y,lst) :
    if (1 <= x <= row) and (1 <= y <= col) :
        return lst[x][y]
    else :
        return False

#----main----
K = int(input())
col, row = map(int, input().split())
i_map = list(map(lambda x : x.strip(), sys.stdin.readlines()))

lst_map = [False]
for r in i_map :
    lst_map.append([False] + list(map(lambda x : not bool(int(x)), r.split())))

goal = row*col
temp = [False]+[list([False for _ in range(K+1)]) for idx in range(col)]
check = [False]+[list(copy.deepcopy(temp)) for idx in range(row) ]
check[1][1] = [True] * (K+1)

q = []  
flag = True
for nx,ny in zip([0,1,0,-1], [-1,0,1,0]) :
    new_x = 1+nx
    new_y = 1+ny
    
    if checkingMatrix(new_x, new_y, lst_map) :
        check[new_x][new_y][K] = True
        q.append((new_x, new_y, 1, K))

if K > 0 :
    for nx,ny in zip([-2,-1,1,2,2,1,-1,-2], [1,2,2,1,-1,-2,-2,-1]) :
        new_x = 1+nx
        new_y = 1+ny
        
        if checkingMatrix(new_x, new_y, lst_map) :
            if not check[new_x][new_y][K-1] :
                check[new_x][new_y][K-1] = True
                q.append((new_x, new_y, 1, K-1))

while (q and flag):
    follow = q.pop(0)
    x, y = follow[0], follow[1]
    cnt = follow[2]
    h_num = follow[3]

    for nx, ny in zip([0,1,0,-1], [-1,0,1,0]) :
        new_x = x+nx
        new_y = y+ny
        
        if checkingMatrix(new_x, new_y, lst_map) :
            if not check[new_x][new_y][h_num] :
                check[new_x][new_y][h_num] = True
                q.append((new_x, new_y, cnt+1, h_num))

                if (new_x == row) and (new_y == col) :
                    print(cnt+1)
                    flag = False
                    break
        
    if h_num > 0 :
        for nx,ny in zip([-2,-1,1,2,2,1,-1,-2], [1,2,2,1,-1,-2,-2,-1]) :
            new_x = x+nx
            new_y = y+ny
            
            if checkingMatrix(new_x, new_y, lst_map) :
                if not check[new_x][new_y][h_num-1] :
                    check[new_x][new_y][h_num-1] = True
                    q.append((new_x, new_y, cnt+1, h_num-1))

                    if (new_x == row) and (new_y == col) :
                        print(cnt+1)
                        flag = False
                        break

if flag :
    print(-1)
