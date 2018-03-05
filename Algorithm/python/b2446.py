num = int(input())

for idx in range(num, 0, -1) :
    print(" "*(num-idx) + "*"*(2*num -1 -2*(num-idx)))

for idx in range(2, num+1) :
    print(" "*(num-idx) + "*"*(2*num -1 -2*(num-idx)))
