from collections import defaultdict

class Robot() :
    def __init__(self, map_dic, s_cord, k_cord_lst, n, k) :
        self.map_dic = map_dic
        self.start_cord = s_cord
        self.key_cord_lst = k_cord_lst
        self.num = n
        self.key = k
        self.distance = defaultdict(lambda : float("inf"))
        self.graph = defaultdict(lambda : set([]))

    def bfs(self, cord) :
        lst = self.getSide(cord)
        self.distance[cord]=0
        
        stayed_lst = list(lst)
        for idx in stayed_lst :
                self.distance[idx] = 1

        count = 2
        
        while lst :
            stayed_lst.pop(0)
            new_lst = self.getSide(lst.pop(0))
            
            for idx in new_lst :
                self.distance[idx] = count
                
            lst.extend(new_lst)

            if not stayed_lst :
                count += 1
                stayed_lst = list(lst)
            
    def getSide(self, cord) :
        r,c = cord
        lst = []

        for v, h in [(0,1), (0,-1), (1,0), (-1,0)] :
            new_r, new_c = r+v, c+h
            temp = (new_r, new_c)
            p = self.map_dic[temp]
            
            if (p != "1") and (self.distance[temp] == float("inf")):
                lst.append(temp)
                
        return lst

    def is_root(self) :
        self.bfs(self.start_cord)
        
        if any(self.distance[x] == float("inf") for x in self.key_cord_lst) :
            return False
        else :
            return True

    def getDistance(self) :
        lst = list([self.start_cord] + self.key_cord_lst)

        for idx1, cord1 in enumerate(lst) :
            self.distance = defaultdict(lambda : float("inf"))
            self.bfs(cord1)
            
            for idx2, cord2 in enumerate(lst) :
                if idx1 != idx2 :
                    self.graph[idx1].add((idx2, self.distance[cord2]))

    def prim(self) :        
        start = 0
        visited = [False] * (len(self.graph))
        visited[start] = True
        total = 0

        for _ in range(len(self.graph) ):
            lst = []
            for idx, bool in enumerate(visited) :
                if bool :
                    lst.extend(list(self.graph[idx]))

            lst = sorted(lst, key = lambda x : x[1])
    
            for x in lst :
                if not visited[x[0]] :
                    visited[x[0]] = True
                    total += x[1]
                    break
                    
                    
                
        return total
        

#--main--
n, k = map(int, input().split())

map_dic = {}
start_cord = (0,0)
key_cord_lst = []
for idx in range(n) :
    for idx2, v in enumerate(input()) :
        map_dic[(idx, idx2)] = v

        if v == "S" :
            start_cord = (idx, idx2)
        elif v == "K" :
            key_cord_lst.append((idx, idx2))

robot = Robot(map_dic, start_cord, key_cord_lst, n, k)

if robot.is_root() :
    robot.getDistance()
    print(robot.prim())
else :
    print(-1)
