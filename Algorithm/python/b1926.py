#remove를 사용할 경우, 앞에서 부터 하나 씩 찾는 것이므로 오히려 시간이 더 걸림
import sys
sys.setrecursionlimit(1000000)

class Picture() :

    def __init__(self, total_dic, row, col) :
        self.total_dic = dict(total_dic)
        self.row = row
        self.col = col
        self.count_lst = []
        self.count = 0
    
    def dfs(self, node) :
            
        r,c = node
        self.count += 1

        for ori in [(-1,0),(1,0),(0,-1),(0,1)] :
            hor, ver = ori
            new_r, new_c = r+hor, c+ver
            temp = (r+hor, c+ver)
            
            if  (0 < new_r < self.row+1) and (0 < new_c < self.col+1) :
                if self.total_dic[temp] :
                    self.total_dic[temp] = False
                    self.dfs(temp)

    def startingDFS(self) :
        
        for key in self.total_dic.keys() :
            if self.total_dic[key] :
                self.total_dic[key] = False
                self.dfs(key)

                self.count_lst.append(self.count)
                self.count = 0
            
        return self.count_lst

    
#--main--
row, col = map(int, input().split())
matrix = list(map(lambda x : x.strip(), sys.stdin.readlines()))

total_dic = {}
for idx, r in enumerate(matrix) :
    for idx2, v in enumerate(r.split()) :
        total_dic[(idx+1, idx2 +1)] = (int(v) == 1)

check = len([x for x in total_dic.values() if x])
if check > max(row, col) * (min(row,col)-1) :
        print(1)
        print(check)
else :
    picture = Picture(total_dic, row, col)
    result = picture.startingDFS()
    
    if result :
        print(len(result))
        print(max(result))
    else :
        print(0)
        print(0)
