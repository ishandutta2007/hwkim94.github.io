lst = list(map(int, input().split()))
lst.sort()
dic = {"A" : lst[0], "B" : lst[1], "C" : lst[2]}

order = input()

for idx in order :
    print(dic[idx], end = " ")

