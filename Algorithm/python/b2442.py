num = int(input())

for idx in range(1, num+1) :
    print((" "*(num-idx))+ ("*"*(1+2*(idx-1))))
