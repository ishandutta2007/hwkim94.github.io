c= int(input())
for idx in range(c):
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(idx+1, a, b, a+b))
