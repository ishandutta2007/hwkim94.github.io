a = input()
check =[x for x in "abcdefghijklmnopqrstuvwxyz"]

for idx, alphabet in enumerate(a) :
    if alphabet in check :
        check[check.index(alphabet)] = idx

results = list(map(lambda x : -1 if type(x) == str else int(x), check))

for idx,result in enumerate(results) :
    if idx != len(results)-1 :
        print(result, end =" ")
    else :
        print(result)

