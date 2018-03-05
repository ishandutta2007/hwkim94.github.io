import sys

def counting(val) :
    dic = {1:0}
    
    for num in range(2, val+1) :
        dic[num] = dic[num-1] + 1
        
        if num % 3 == 0 and dic[num] > dic[num//3]:
            dic[num] = dic[num//3] + 1
            
        if num % 2 == 0 and dic[num] > dic[num//2]:
            dic[num] = dic[num//2] + 1

    return dic[val]


test = int(sys.stdin.readline())
print(counting(test))

