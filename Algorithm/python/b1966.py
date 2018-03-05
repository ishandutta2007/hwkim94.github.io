import sys

def lst2str(lst) :
    return "".join(list(map(str, lst)))

def printer(lst, target) :
    max_value = max(lst)
    target_value = lst[target]
    
    indexed_lst = []
    for idx, v in enumerate(lst) :
        indexed_lst.append((idx, v))

    #자신이 최대값일 경우
    if max_value == target_value :
        return lst[:target].count(target_value) + 1

    #그 외
    count = 0
    temp1, temp2 = lst[:target], lst[target:]
    
    while max_value > target_value :
        num_max_value = lst.count(max_value)
        latest_index = lst2str(lst).rfind(str(max_value))

        if latest_index < target :
            target -= (latest_index + 1)
        else :
            target += len(lst[latest_index:]) - temp1.count(max_value) - 1
        
        lst = list(lst[latest_index:] + lst[:latest_index])
        lst = list(filter(lambda x : x != max_value, lst))

        temp1, temp2 = lst[:target], lst[target:]
        count += num_max_value
        max_value = max(lst)

        if max_value == target_value :
            return temp1.count(target_value) + count +1
        
num = int(input())
for idx in range(num) :
    page, target = list(map(int, input().split()))
    lst = list(map(int, sys.stdin.readline().split()))
    
    result = printer(lst, target)
    print(result)
