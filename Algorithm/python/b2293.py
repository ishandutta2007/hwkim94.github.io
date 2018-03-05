import sys

n, k = map(int, input().split())
coins = list(map(int, list(map(lambda x : x.strip(), sys.stdin.readlines()))))
memo = {}

for idx in range(k+1) :
    memo[idx] = 0
memo[0] = 1

def count_coin(num,money) :

    for idx in range(num) :
        result = coins[idx]
        
        for idx2 in range(result, money+1) :
            if idx2>= result :       
                memo[idx2] += memo[idx2 -result]
            
    return memo[money]

print(count_coin(n,k))
