num = int(input())

pinary_dic = {1:1, 2:1}
for idx in range(3, num+1) :
    pinary_dic[idx] = sum(pinary_dic.values()) - pinary_dic[idx-1]+1

print(pinary_dic[num])
