from sys import stdin

num  = list(map(int, list(stdin.readline().strip())))

def num_30(lst) :
    if not(0 in lst) or sum(lst)%3 !=0 :
        return -1

    else :
        lst.sort(reverse = True)
        return "".join(str(x) for x in lst)

print(num_30(num))
