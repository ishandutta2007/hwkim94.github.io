#시간초과
import sys

num = int(input())

for idx in range(num) :
    comd = sys.stdin.readline().strip()
    length = int(input())
    lst = eval(sys.stdin.readline().strip())
    n = True

    if comd.count("D") > len(lst) :
        print("error")
        continue
    
    elif comd.count("D") == len(lst) :
        print([])
        continue

    comd = comd.replace("RR", "")

    for c in comd :
        if c == "R" :
            lst.reverse()

        else :
            if not lst :
                print("error")
                n = False
                break
            else :
                lst.pop(0)

    if n :
        print(lst)
    
#정답
#오류 이유 : 출력양식에는 띄어쓰기가 없
import sys

def printer(lst) :
    lst = list(map(str, lst))
    result = "[" + ",".join(lst) + "]"

    return result

num = int(input())

for idx in range(num) :
    comd = sys.stdin.readline().strip()
    length = int(input())
    lst = eval(sys.stdin.readline().strip())

    if comd.count("D") > len(lst) :
        print("error")
        continue
    elif comd.count("D") == len(lst) or (not lst):
        print([])
        continue

    comd = comd.replace("RR", "")

    start = 0
    r_start = 0
    sign = 1
 
    for c in comd :
        if c == "R" :
            sign *= -1

        else :
            if sign > 0 :
                start += 1
            else :
                r_start += 1


    if r_start > 0 :
        result = lst[start:-r_start]
        
        if sign < 0 :
            result.reverse()
       
    else :
        result = lst[start:]
        
        if sign < 0 :
            result.reverse()
        
    print(printer(result))
    


        
