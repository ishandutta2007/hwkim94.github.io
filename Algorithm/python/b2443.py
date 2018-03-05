num = int(input())

for idx in range(num, 0, -1) :
    print((" "*(num-idx))+ ("*"*(1+2*(idx-1))))
