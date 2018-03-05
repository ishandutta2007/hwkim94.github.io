def fibonacci(val) :
    dic = {0:(1,0), 1 :(0,1)}
    for idx in range(2, val+1) :
        first = idx -1
        last = idx -2
        dic[idx] = [dic[first][0] +dic[last][0], dic[first][1] +dic[last][1]]
        
    return dic[val]

num = int(input())

for idx in range(num) :
    val = int(input())
    lst = fibonacci(val)
    print(lst[0], lst[1])
