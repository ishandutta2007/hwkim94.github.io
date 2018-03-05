#방법1
from math import factorial

def counting(num) :
    
    one = num
    two = 0
    three = 0
    lst = [[one, two, three]]

    three_max = num//3
    two_max = (num-three_max*3)//2
    one_max = num - three_max*3 - two_max*2
    
    while lst[-1] != [one_max, two_max, three_max] :
        
        #1이 2개 이상인 경우 2가 하나 들어난다.
        if one >= 2 :
            one -= 2
            two += 1

        #1이 1개 이하인 경우 2를 줄이고 3을 늘린다.
        elif one>=0 :
            three +=1
            two = 0
            one = num - 3*three

        lst.append([one, two, three])

    return lst

def case(lst) :
    count = 0
    
    for idx in lst :
        count += factorial(sum(idx))//(factorial(idx[0]) * factorial(idx[1]) *factorial(idx[2]))

    return count

[print(case(counting(int(input())))) for _ in range(int(input()))]


#방법2
dic = {1:1, 2:2, 3:4}

def counting(val) :
    for idx in range(4, val+1):
        dic[idx] = dic[idx-1] + dic[idx-2] + dic[idx-3]

    return dic[val]

num = int(input())

for idx in range(num) :
    test = int(input())
    print(counting(test))
