num =int(input())
seq = list(map(int, input().split()))
dic = {seq[0] : 1}

for idx in range(1, num) :
    key = seq[idx]
    check = [x for x in list(dic.keys()) if x < key]
    
    if check :
        dic[key] = max([dic[x] for x in check]) +1
    else :
        dic[key] = 1

print(max(dic.values()))
