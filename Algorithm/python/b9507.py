import sys

num = input()
quiz = list(map(lambda x : x.strip(), sys.stdin.readlines()))
quiz = list(map(int, quiz))

M = max(quiz)
dic = {0:1, 1:1, 2:2, 3:4}
for idx in range(4, M+1) :
    dic[idx] = dic[idx-1] + dic[idx-2] + dic[idx-3] + dic[idx-4]

for idx in quiz :
    print(dic[idx])
    
