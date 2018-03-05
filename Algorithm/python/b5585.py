import sys
sys.setrecursionlimit(100000)

dic = {1:1, 5:1, 10:1, 50:1, 100:1, 500:1}
coins = [1, 5, 10, 50, 100, 500]

def coin(val) :
    if val in dic :
        return dic[val]

    else :
        temp = min([coin(val-cn) for cn in coins if (val>cn)]) +1
        dic[val] = temp
        return temp

num = int(input())
print(coin(1000-num))
