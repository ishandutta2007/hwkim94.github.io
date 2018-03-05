a, b = map(int, input().split())

candy = {}
for idx in range(1, a+1) :
    candy[idx] = list(map(int, input().split()))

dic = {(1,1) : candy[1][0]}
for idx in range(2, a+1) :
    dic[(idx, 1)] = dic[(idx-1, 1)] + candy[idx][0]

for idx in range(2, b+1) :
    dic[(1, idx)] = dic[(1, idx-1)] + candy[1][idx-1]
    
for idx in range(2, a+1) :
    for idx2 in range(2, b+1) :
        dic[(idx, idx2)] = max(dic[(idx-1, idx2-1)], dic[(idx, idx2-1)], dic[(idx-1, idx2)]) + candy[idx][idx2-1]


print(dic[(a,b)])
