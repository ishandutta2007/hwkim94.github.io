#방법1
num =int(input())
seq = list(map(int, input().split()))

dic ={1 : seq[0]}

for idx in range(2, num+1) :
    dic[idx] = max(dic[idx-1] + seq[idx-1], seq[idx-1])
    
print(max(dic.values()))


#방법2
num =int(input())
seq = list(map(int, input().split()))

max_num = seq[0]
best = max_num

for idx in range(1, num) :
    max_num = max(max_num + seq[idx], seq[idx])
    best = max(max_num, best)
print(best)


