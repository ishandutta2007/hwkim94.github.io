string = input()
result= [string[x:] for x in range(len(string)) ]


result.sort()

for idx in result :
    print(idx)


