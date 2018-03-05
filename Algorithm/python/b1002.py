import math

def find_location(x1,y1,r1, x2,y2,r2) :
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    #중점이 같을 경우
    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            return -1
        else :
            return 0

    #한 점에서 만나는 경우
    if (r1 + r2) == d or abs(r2 - r1) == d:
        return 1

    #만나지 않는 경우
    if r1 + r2 < d or abs(r2 - r1) > d:
        return 0

    #그 외의 모든 경우는 두 점에서 만나게 
    return 2
        
num = int(input())

for idx in range(num) :
    a,b,c,d,e,f = map(int, input().split())
    print(find_location(a,b,c,d,e,f))
