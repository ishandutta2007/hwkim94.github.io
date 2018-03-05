num =int(input())
seq = list(map(int, input().split()))
dic = {seq[0] : seq[0]}

for idx in range(1, num) :
    key = seq[idx]
    check = [x for x in list(dic.keys()) if x < key]
    
    if check :
        dic[key] = max([dic[x] for x in check]) + key
    else :
        dic[key] = key

print(max(dic.values()))
