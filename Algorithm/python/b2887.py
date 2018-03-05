#-----시간 초과 안걸리는 코드-----
#prim

import sys
import operator

class Graph() :
    def __init__(self, num) :
        self.vertex = {}
        self.path = {}
        self.num = num
        
    def add(self, num, a, b, c) :
        self.vertex[num] = [a,b,c]
        self.making_path(num)

    def making_path(self, ver) :
        lst = list(self.vertex.keys())
        lst.remove(ver)
        
        for idx in lst :
            a = self.vertex[idx]
            b = self.vertex[ver]
            self.path[(idx, ver)] = min(abs(a[0] -b[0]), abs(a[1] -b[1]), abs(a[2] -b[2]))

    def mst_prim(self) :
        start = 1
        checked_vertex = set([1])

        temp = [(item[0],item[1]) for item in self.path.items() if (start in item[0])]
        print(temp)
        first_path = sorted(temp, key=operator.itemgetter(1))[0]
        path_length = first_path[1]
        checked_vertex.update(first_path[0])
        
        for _ in range(num-2) :
            self.path = {k:v for k,v in self.path.items() if not ((k[0] in checked_vertex) & (k[1] in checked_vertex))}
            temp = [(item[0], item[1]) for item in self.path.items() if (any((key2 in checked_vertex) for key2 in item[0]))]
            temp = sorted(temp, key=operator.itemgetter(1))[0]
            checked_path = temp
            path_length += checked_path[1]
            checked_vertex.update(checked_path[0])
            
        return path_length
        
num =  int(input())
planets = list(map(lambda x : x.strip(), sys.stdin.readlines()))

graph =Graph(num)

for idx, planet in enumerate(planets) :
    a,b,c = map(int, planet.split())
    graph.add(idx+1, a, b, c)

print(graph.mst_prim())

#-----시간 초과 안걸리는 코드-----
#kruskal
import sys
import operator

class Graph() :
    def __init__(self, num) :
        self.vertex = {}
        self.path = {}
        self.num = num
        
    def add(self, num, val1, val2, val3) :
        self.vertex[num] = [val1, val2, val3]
        
    def making_path(self) :
        lst = list(self.vertex.items())
        
        x_lst = sorted(lst, key = lambda x: x[1][0])
        for idx in range(self.num-1) :
            a, b = x_lst[idx], x_lst[idx+1]
            self.path[(a[0],b[0])] = abs(a[1][0] -b[1][0])
                
                
        y_lst = sorted(lst, key = lambda x: x[1][1])
        for idx in range(self.num-1) :
            a, b = y_lst[idx], y_lst[idx+1]
            temp_path = abs(a[1][1] -b[1][1])
            temp_vertex1, temp_vertex2 = (a[0],b[0]), (b[0],a[0])
            
            if temp_vertex1 in self.path :
                if temp_path <= self.path[temp_vertex1] :
                    self.path[temp_vertex1] = temp_path
            elif temp_vertex2 in self.path :
                if temp_path <= self.path[temp_vertex2] :
                    self.path[temp_vertex2] = temp_path
            else :
                self.path[temp_vertex1] = temp_path


        z_lst = sorted(lst, key = lambda x: x[1][2])
        for idx in range(self.num-1) :
            a, b = z_lst[idx], z_lst[idx+1]
            temp_path = abs(a[1][2] -b[1][2])
            temp_vertex1, temp_vertex2 = (a[0],b[0]), (b[0],a[0])
            
            if temp_vertex1 in self.path :
                if temp_path <= self.path[temp_vertex1] :
                    self.path[temp_vertex1] = temp_path
            elif temp_vertex2 in self.path :
                if temp_path <= self.path[temp_vertex2] :
                    self.path[temp_vertex2] = temp_path
            else :
                self.path[temp_vertex1] = temp_path

    def mst_kruskal(self) :
        lst = sorted(list(self.path.items()), key = lambda x : x[1])
        total_cost = 0
        rank = [0] * (self.num+1)
        parent = list(range(self.num+1))
        MST = []

        #자신이 어떤 그룹에 속해있는지 찾아주는 함수
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]

        #속한 그룹을 합쳐주는 함수
        def union(x, y) :
            xr = find(x)
            yr = find(y)

            #이 경우는 예외상황
            if xr == yr :
                return

            #rank가 더 큰 것으로 바꿔줌
            if rank[xr] < rank[yr] :
                parent[xr] = yr

            elif rank[xr] > rank[yr] :
                parent[yr] = xr

            else :
                parent[yr] = xr
                rank[xr] += 1

        for path in lst :
            ver1, ver2 = path[0]
            cost = path[1]

            if find(ver1) != find(ver2) :
                total_cost += cost
                union(ver1, ver2)
                MST.append(path)

                if len(MST) == num :
                    return total_cost
            
        return total_cost
#-----------
        
num =  int(input())
planets = list(map(lambda x : x.strip(), sys.stdin.readlines()))

graph =Graph(num)

for idx, planet in enumerate(planets) :
    a,b,c = map(int, planet.split())
    graph.add(idx+1, a, b, c)
    
graph.making_path()
print(graph.mst_kruskal())
