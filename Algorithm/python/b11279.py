import sys

def last_0(lst) :
    if 0 in lst :
        return list(lst)[:(len(lst) - lst[::-1].index(0))]
    else :
        return []

class Max_Heap() :
    def __init__(self) :
        self.heap = []

    def push(self, num) :
        index = self.find_index(num)
        
        if index != -1 :
            self.heap.insert(index,num)
        else :
            self.heap.append(num)
        
    def pop(self) :
        if self.heap :
            return self.heap.pop()
        else :
            return 0 
        
    def sorting(self) :
        self.heap.sort()

    def find_index(self, num) :
        length = len(self.heap)
        index = length//2

        if length == 0 :
            return -1

        if length == 1 :
                if self.heap[0] > num :
                    return index 
            
                else :
                    return index + 1

        while length :
            left, right = length//2, length - length//2
            
            if length == 1 :
                if self.heap[left-1] > num :
                    return index 
            
                else :
                    return index + 1
             
            
            if self.heap[index-1] > num :
                length = left
                index -= (left - length//2)
                
            elif self.heap[index-1] <num :
                length = right
                index += length//2
                
            else :
                return index
            

#--실행부--
num =int(input())
data = list(map(lambda x: int(x.strip()),sys.stdin.readlines()))

cmds = last_0(data)
max_heap = Max_Heap()

for cmd in cmds :
    if cmd ==0 :
        print(max_heap.pop())
    else :
        max_heap.push(cmd)







