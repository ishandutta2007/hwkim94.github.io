#풀이1, dic 사용
num = int(input())
memo = {0:0, 1:1, 2:3}

for idx in range(3, num+1) :
    memo[idx] = memo[idx-1] + 2*memo[idx-2]

print(memo[num]%10007)

#풀이2, lst 사용, 용량 면에서 이득일 것이라 생각했지만 차이가 없었음
num = int(input())
memo = [0,1,3]

for idx in range(3, num+1) :
    memo.append(memo[idx-1] + 2*memo[idx-2])

print(memo[num]%10007)
