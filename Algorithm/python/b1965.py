import sys

num = int(input())
line = list(map(int, sys.stdin.readline().strip().split()))

lst = [(line[0], 1)]

m = line[0] # 가장 작은 박스의 크기
M = line[0] # 가장 많이 들어간 박스의 크기
M_num = 1 # 가장 많이 들어간 박스의 개수

for idx in line[1:] :
    lst.sort(reverse = True)
    
    if idx in [m, M] :
        continue

    if idx > M :
        M_num += 1
        M = idx
        lst.append((M, M_num))
        continue
    
    if idx < m :
        m = idx
        lst.append((m, 1))
        continue


    temp = sorted(list(filter(lambda x : x[0] < idx, lst)), key = lambda x : x[1])[-1][1]
    value = temp + 1
    lst.append((idx, value))

    if value > M_num :
        M_num = value
        M = idx
        continue

    if (value == M_num) and (idx < M):
        M = idx
        continue

print(M_num)

#다른 방법, 위 방법보다 더 빠름
import sys

class NewQueue() :
    def __init__(self, lst) :
        self.queue = lst
        self.max = 1

    def insert(self, elts) :
        find = False
        for idx, val in enumerate(self.queue) :
            if elts > val[0] and not find :
                index = idx 
                m = val[1]
                find = True
                
            if find and m < val[1]:
                m = val[1]

        self.queue.insert(index, (elts, m+1))
        if m+1 > self.max :
            self.max = m+1
                
    def append(self, elts) :
        self.queue.append((elts, 1))

    def get(self) :
        return self.max
        
num = int(input())
line = list(map(int, sys.stdin.readline().strip().split()))

lst = NewQueue([(line[0], 1)])
m = line[0]

for idx in line[1:] : 
    if idx == m :
        continue
    
    if idx < m :
        m = idx
        lst.append(m)
        continue

    lst.insert(idx)

print(lst.get())

#다른 방법2, 위 방법보다 더 빠름
import sys

class NewQueue() :
    def __init__(self, lst) :
        self.queue = lst
        self.max = 1

    def insert(self, elts) :
        index = self.binary_search(elts)
        m = 0
        for idx in self.queue :
            if elts <= idx[0]:
                break
            
            if m < idx[1] :
                m = idx[1]
        
        if m >= self.max :
            self.max = m+1

        self.queue.insert(index, (elts, m+1))

    def append(self, elts) :
        self.queue.insert(0, (elts, 1))

    def get(self) :
        return self.max

    def binary_search(self, target):
        start = 0
        end = len(self.queue) -1

        if end == 0 :
            return 1

        while start < end:
            mid = (start + end) // 2

            if self.queue[mid][0] == target:
                return mid 
            
            elif self.queue[mid][0] < target:
                start = mid + 1

            elif self.queue[mid][0] > target:
                end = mid -1
                
        if start == end :
            if self.queue[start][0] > target :
                return start
            
            else :
                return start+1

        else :
            if self.queue[end][0] > target :
                return end
            
            else :
                return end+1
        
num = int(input())
line = list(map(int, sys.stdin.readline().strip().split()))

lst = NewQueue([(line[0], 1)])
m = line[0]

for idx in line[1:] : 
    if idx == m :
        continue
    
    if idx < m :
        m = idx
        lst.append(m)
        continue

    lst.insert(idx)

print(lst.get())










        


