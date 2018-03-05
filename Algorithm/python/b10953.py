c= int(input())
for idx in range(c):
    a, b = map(int, input().replace(",", " ").split())
    if a == 0 and b ==0 :
        break
    print(a+b)
