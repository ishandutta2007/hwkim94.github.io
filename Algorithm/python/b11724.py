#연결되지 않은 점은 그냥 그대로 하나의 간선이 됨을 유의
import sys

class Graph() :
    def __init__(self, n) :
        self.point = n
        self.connected_point_lst = set([])
        self.road = []

    def add_lst(self, a, b) :
        if (a in self.connected_point_lst) and (b in self.connected_point_lst) :
            self.add_road_1(a,b)
            
        elif (a in self.connected_point_lst) or (b in self.connected_point_lst) :
            self.connected_point_lst.update([a, b])
            self.add_road_2(a, b)

        else :
            self.connected_point_lst.update([a, b])
            self.add_road_3(a,b)

    def add_road_1(self, a, b) :
        idx_a = self.get_idx(a)
        idx_b = self.get_idx(b)

        if idx_a != idx_b :
            new_a, new_b = self.road[idx_a], self.road[idx_b]
            new_road = new_a | new_b
            self.road.remove(new_a)
            self.road.remove(new_b)
            self.road.append(new_road)
        
    def add_road_2(self, a, b) :
        for idx, road in enumerate(self.road) :
            if (a in road) or (b in road) :
                self.road[idx].update([a,b])
                break
        
    def add_road_3(self, a, b) :
        self.road.append({a, b})

    def get_idx(self, a) :
        for idx, road in enumerate(self.road) :
            if a in road :
                return idx
            
    def count_road(self) :
        if len(self.connected_point_lst) == self.point :
            return len(self.road)
        else :
            return len(self.road) + (self.point - len(self.connected_point_lst) )
    
n, m = map(int, input().split())
roads = list(map(lambda x : x.strip(), sys.stdin.readlines()))
graph = Graph(n)

for road in roads :
    start, finish = map(int, road.split())
    graph.add_lst(start, finish)

print(graph.count_road())

        
#----bfs----
import sys
from collections import defaultdict
N,M = map(int, sys.stdin.readline().split())

V = defaultdict(lambda: [])

for i in range(M):
    s,e = map(int, sys.stdin.readline().split())

    V[s].append(e)
    V[e].append(s)

ans = 0
check = defaultdict(lambda: False)
def bfs(root):
    q = []
    check[root] = True
    q.append(root)

    while len(q) != 0:
        x = q[0]
        q.pop(0)

        for y in V[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

for i in range(1, N+1):
    if check[i] == False:
        ans += 1
        bfs(i)

print(ans)


#----dfs----
import sys
from collections import defaultdict
sys.setrecursionlimit(100000)

N,M = map(int, sys.stdin.readline().split())

V = defaultdict(lambda: [])

for i in range(M):
    s,e = map(int, sys.stdin.readline().split())

    V[s].append(e)
    V[e].append(s)

ans = 0
check = defaultdict(lambda: False)

def dfs(x):
    check[x] = True
    for y in V[x]:
        if check[y] == False:
            dfs(y)

for i in range(1, N+1):
    if check[i] == False:
        ans += 1
        dfs(i)

print(ans)
