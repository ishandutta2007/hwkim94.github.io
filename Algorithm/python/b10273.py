#dict, defaultdict는 메모리 낭비가 심하므로 lst를 False로 사용하기
#이미 사용한 것은 버리기

import sys
sys.setrecursionlimit(100000)

class Cave() :
    def __init__(self, dic, topology_path, money, n) :
        self.info_dic = dic
        self.money_lst = money
        self.topology_path = topology_path
        
        self.result_path = [False] *(n+1)
        self.result_money = [False] * (n+1)
        self.best = (money[1], [1])
        self.visited = [False] * (n+1)
        
    def is_root(self) :
        if not self.info_dic[1] :
            return False
        else :
            return True

    def dfs(self, start) :
        self.visited[start] = True
        can_go_lst = self.info_dic[start]
        
        if can_go_lst :
            for idx in can_go_lst :
                temp = idx[0]
                
                if not self.visited[temp] :
                    self.dfs(temp)

    def filtering(self) :

        for idx, val in enumerate(self.visited) :
            if val :
                self.result_path[idx] = []
                self.result_money[idx] = -10001
            

    def topological_sort(self) :
        lst = [1]
        self.result_money[1] = self.money_lst[1]
        self.result_path[1].append(1)

        while lst :
            start = lst.pop(0)
            can_go_lst = self.info_dic[start]
            
            if not can_go_lst :
                continue
            
            for node, cost in can_go_lst:
                
                self.topology_path[node] += -1
                earned = self.result_money[node]
                new_earned = self.result_money[start] + self.money_lst[node] - cost

                if earned < new_earned :
                    self.result_money[node] = new_earned
                    self.result_path[node] = self.result_path[start] + [node]
            
                if new_earned > self.best[0] :
                    self.best = (new_earned, self.result_path[node])

                if not self.topology_path[node] :
                    lst.append(node)
                    
            self.info_dic[start] = False
            self.result_path[start] = False
            self.result_money[start] = False

        return self.best
#--main--
for _ in range(int(input())) :
    n, m = map(int, sys.stdin.readline().split())
    info_dic = [False] *(n+1)
    topology_path = [0] * (n+1)

    money_lst = list(map(int, sys.stdin.readline().split()))
    money_lst = [0] + money_lst
    
    for __ in range(m) :
        a,b,c = map(int, sys.stdin.readline().split())
    
        if info_dic[a] :
            info_dic[a].append((b,c))
        else :
            info_dic[a] = [(b,c)]
            
        topology_path[b] += 1
    
    cave = Cave(info_dic, topology_path, money_lst, n)
    
    if cave.is_root() :
        cave.dfs(1)
        cave.filtering()
        money, caves = cave.topological_sort()
        
        print(money, len(caves))
        print(" ".join(map(lambda x : str(x), caves)))
        
    else :
        print(money_lst[1], 1)
        print(1)
