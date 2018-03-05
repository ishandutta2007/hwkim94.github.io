import sys
import copy

#---------------------
class Graph() :
    def __init__(self, g_list, num) :
        self.list = g_list
        self.result_list = {}
        self.length = num
                    
    def finding(self, row, road) :
        added_road = set([])
        result = set(road)
        
        for idx in road :
            if idx in self.result_list :
                result.update(self.result_list[idx])
            else :
                added_road.update(self.list[idx])
            
        check = added_road - result
        result.update(check)
        added_road = set([])
        
        while check :
            for idx in check :
                added_road.update(self.list[idx])
            
            check = added_road - result

            result.update(check)
            added_road = set([])

        return result
            
    def making_result(self) :
        for idx in range(1, self.length+1) :
            self.result_list[idx] = self.finding(idx, set(self.list[idx]))
            
    def making_matrix(self) :
        for idx, val in enumerate(self.result_list.values()) :
            temp = [0]* self.length
            
            for idx2 in val :
                temp[idx2-1] = 1
            self.result_list[idx+1] = temp


#---------------------행렬 입력받기(인접 리스트로 전환)
num = int(input())
i_matrix = list(map(lambda x : x.strip(), sys.stdin.readlines()))

i_dic = {}
for idx, rows in enumerate(i_matrix) :
    row = rows.split()
    i_dic[idx+1] = set([(idx +1) for idx, path in enumerate(row) if path=="1"])

#---------------------연산
graph = Graph(i_dic, num)
graph.making_result()
graph.making_matrix()


#---------------------결과 출력
[print(" ".join(map(str, idx))) for idx in graph.result_list.values()]


  
