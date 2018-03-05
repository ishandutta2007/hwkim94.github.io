num = int(input())
dic = {}
lst = []
for idx in range(num) :
    value = input()

    try :
        int(value)
    except :
        pass
    else :
        continue

    lst.append(value)
    
lst = list(set(lst))
lst.sort()

for value in lst :
    if len(value) in dic :
        dic[len(value)].append(value)

    else :
        dic[len(value)] = [value]

to_sort = [x for x in dic]
to_sort.sort()
result = []

for idx in to_sort :
    result = result + dic[idx]
    
for idx in result :
    print(idx)
