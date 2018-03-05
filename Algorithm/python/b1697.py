class Graph() :
    def __init__(self, a, b) :
        self.a = a
        self.b = b
        
        if a > 1 :
            self.start = a // 2
        else :
             self.start = a
             
        self.end = b * 2

        if self.end > 100000 :
            self.end = 100000
        
        self.road = {}
        self.table = {}

    def making_graph(self) :
        for idx in range(self.start, self.end+1) :
            self.road[idx] = set(filter(lambda x : (x>=self.start) | (x<=self.end), [idx-1, idx+1, idx*2]))
        
    def finding(self) :
        result = set(self.road[self.a])
        added_road = set([])
        path_min = 11111111111111111111
        
        count = 0

        # a에서 b를 바로 갈 수 있는 경우, 한 번만에 가는 것이 무조건 최소이므로
        # 1을 반환하고 종료
        if self.b in  result:
            return 1
        count += 1

        # a에서 b를 바로 갈 수 없는 경우, 갈 수 있는 루트를 탐색
        for idx in result :

            # 제한범위 안에 있는 경로만 탐색
            if idx <= self.start or idx >= self.end :
                continue
               
            # 탐색해야할 리스트에 포함시켜줌
            new = list(filter(lambda x : x<=self.end | x>= self.start , self.road[idx]))

            if self.b in new :
                if (count+1) < path_min :
                    path_min = count+1
                new.remove(self.b)
                
            added_road.update(new)
        count += 1

        # 탐색해야할 경로 준비         
        check = added_road - result
        result.update(check)
        added_road = set([])

        
        #탐색 시작
        while check :
            
            for idx in check :              
                if idx < self.start or idx > self.end :
                    continue
                
                new = list(filter(lambda x : x<=self.end | x>= self.start , self.road[idx]))

                if self.b in new :
                    if (count+1) < path_min :
                        path_min = count+1
                    new.remove(self.b)

                added_road.update(new) 
            check = added_road - result
            
            result.update(check)
            added_road = set([])
            count+=1

        return path_min

a, b = map(int, input().split())

if a == b :
    print(0)

elif a > b :
    print(a-b)
    
else :
    graph = Graph(a, b)
    graph.making_graph()
    ans = graph.finding()
    print(ans)
