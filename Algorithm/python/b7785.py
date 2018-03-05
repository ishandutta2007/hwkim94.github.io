import sys

num = int(sys.stdin.readline().split()[0])

dic= {}
for idx in range(num) :
    i=sys.stdin.readline().split()
    name, state = i[0], i[1]
    
    if state == "enter" :
        dic[name] = 1
    else :
        dic[name] = 2

lst = [name for name,state in dic.items() if state ==1]

lst.sort(reverse=True)
print("\n".join(lst))


    
