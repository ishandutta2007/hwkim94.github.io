import sys
sys.setrecursionlimit(100000)

import sys

n, k = map(int, input().split())
coins = list(map(int, list(map(lambda x : x.strip(), sys.stdin.readlines()))))
memo = {}

for coin in coins :
    memo[coin] = 1

def count_coin(money) :
    if money in memo.keys() :
        return memo[money] 

    else :
        searched_lst = [count_coin(money - coin) for coin in coins if coin < money ]

        if searched_lst :
            result = min(searched_lst) +1
            memo[money] = result
            return result
        else :
            return 2**31+1


result =count_coin(k)
if result > 2**31 :
    print(-1)
else :
    print(result)
