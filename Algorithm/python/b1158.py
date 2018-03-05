a , b = map(int, input().split())
start = [(x+1) for x in range(a)]
finish = []

idx = b
count = a
while  count:
    if idx > len(start) :
        start += start[-count:]
        continue
    else :
        finish.append(start.pop(idx-1))
        idx += (b - 1)
        count -= 1

print("<", end='')
for idx2, num in enumerate(finish) :
    if idx2 != len(finish)-1 :
        print(num, end=", ")
    else :
        print(num, end="")
print(">")
