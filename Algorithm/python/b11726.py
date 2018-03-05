from math import factorial

def rectangle(num) :
    one = num
    two = 0

    max_two = num//2
    max_one = num - max_two*2

    lst = [[one, two]]

    for idx in range(max_two) :
        one -= 2
        two +=1
        lst.append([one, two])

    total = 0
    for idx in lst :
        total += factorial(sum(idx)) //(factorial(idx[0]) * factorial(idx[1]))

    return total%10007

print(rectangle(int(input())))

#DP
num = int(input())
dic = {0 : 0, 1 : 1, 2:2}

for idx in range(3, num+1) :
    dic[idx] = dic[idx-1] + dic[idx-2]

print(dic[num]%10007)
