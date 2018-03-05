num = int(input())

for idx in range(1, num+1) :
    print("*"*idx + " "*2*(num-idx) + "*"*idx)

for idx in range(num-1, 0, -1) :
    print("*"*idx + " "*(num*2-2*idx) + "*"*idx)
