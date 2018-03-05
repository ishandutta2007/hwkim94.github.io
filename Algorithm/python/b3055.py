class Graph() :
    def __init__(self, r_num, c_num, maps) :
        self.maps = {}
        self.row_num = r_num
        self.col_num = c_num
        
        self.destination = 0
        self.start = 0
        self.water = set([])
        self.rock = []

        forests = " "
        for place in maps :
            forests += place

        for idx in range(1, self.row_num*self.col_num+1) :
            self.maps[idx] = set([])

            s1 = idx - self.col_num #상
            s2 = idx + self.col_num #하
            s3 = idx - 1            #좌
            s4 = idx + 1            #우

            now = forests[idx]

            if now == "D" :
                self.destination = idx
                del self.maps[idx]
                continue
            
            elif now == "S" :
                self.start = idx
            
            elif now == "X" :
                self.rock.append(idx)
                del self.maps[idx]
                continue
            
            elif now == "*" :
                self.water.update([idx])
                del self.maps[idx]
                continue
            
                
            if s1 > 0 :
                if forests[s1] in (".", "D", "S") :
                    self.maps[idx].update([s1])

            if s2 < self.row_num * self.col_num+1 :
                if forests[s2] in (".", "D", "S") :
                    self.maps[idx].update([s2])
                    
            if s3 % self.col_num != 0 :
                if forests[s3] in (".", "D", "S") :
                    self.maps[idx].update([s3])

            if s4 % self.col_num != 1 :
                if forests[s4] in (".", "D", "S") :
                    self.maps[idx].update([s4])

    def delete(self) :
        new_water = set([])
        
        for idx in self.water :
            s1 = idx - self.col_num #상
            s2 = idx + self.col_num #하
            s3 = idx - 1            #좌
            s4 = idx + 1            #우
            
            if s1 > 0 :
                if s1 in self.maps.keys() :
                    new_water.update([s1])

            if s2 < self.row_num * self.col_num+1 :
                if s2 in self.maps.keys() :
                    new_water.update([s2])
                    
            if s3 % self.col_num != 0 :
                if s3 in self.maps.keys() :
                    new_water.update([s3])

            if s4 % self.col_num != 1 :
                if s4 in self.maps.keys() :
                    new_water.update([s4])

        for idx in self.maps.keys() :
            self.maps[idx] = set(self.maps[idx] - new_water)
            
        for idx in new_water :
            del self.maps[idx]
            
        self.water.update(new_water)

    def bfs(self) :
        count = 0

        need_to_search = set(self.maps[self.start])
        self.delete()
        need_to_search = [x for x in need_to_search if not x in self.water]
        count +=1
        
        if self.destination in need_to_search :
            return count

        #굴이 둘러쌓여 있을 경우
        idx = self.destination
        s1 = idx - self.col_num #상
        s2 = idx + self.col_num #하
        s3 = idx - 1            #좌
        s4 = idx + 1            #우
                    
        while need_to_search :
            count += 1

            search = list(need_to_search)
            need_to_search = set([])
            for idx in search :
                need_to_search.update(self.maps[idx])
                if self.destination in need_to_search :
                    return count
                
            self.delete()
            need_to_search = [x for x in need_to_search if not x in self.water]
            flag=0
    
            if s1 > 0 :
                if s1 not in self.maps.keys() :
                    flag +=1
            else :
                flag+=1

            if s2 < self.row_num * self.col_num+1 :
                if s2 not in self.maps.keys() :
                    flag +=1
            else :
                flag+=1
                            
            if s3 % self.col_num != 0 :
                if s3 not in self.maps.keys() :
                    flag +=1
            else :
                flag+=1
                        
            if s4 % self.col_num != 1 :
                if s4 not in self.maps.keys() :
                    flag +=1
            else :
                flag+=1
                
            if flag ==4 :
                return "KAKTUS"

        return "KAKTUS"

#-----
a, b = map(int, input().split())

rows =[]
for idx in range(a) :
    row = input()
    rows.append(row)

graph = Graph(a, b, rows)
print(graph.bfs())
