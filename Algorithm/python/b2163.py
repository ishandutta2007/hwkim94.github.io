#----1번----
#더 많은 쪽을 잘라야
i_max, i_min = sorted(list(map(int, input().split())), reverse = True)
choco ={(1,1) : 0}

num =  i_max * (i_max-1) // 2 + i_min
a, b = 1, 1

for idx in range(num-1) :
    if a == b :
        a += 1
        b = 1
        
        if a % 2 == 0 :
            choco[(a,b)] = choco[(a//2, b)] * 2 + 1
        else :
            choco[(a,b)] = choco[(a//2, b)] + choco[(a//2 + 1, b)] + 1

    else :
        b += 1

        if a % 2 == 0 :
            temp_a, temp_b = sorted([a//2, b], reverse = True)
            choco[(a,b)] = choco[(temp_a, temp_b)] * 2 + 1
        else :
            temp_a = a//2
            temp_a1, temp_a2 = temp_a+1, temp_a

            if b >= temp_a1 :
                choco[(a,b)]  = choco[(b, temp_a1)] + choco[(b, temp_a2)] + 1
            else :
                choco[(a,b)] = choco[(temp_a1, b)] + choco[(temp_a2, b)] + 1

print(choco[(i_max, i_min)])

#----2번----
#증명필요!!!
i_max, i_min = map(int, input().split())
print(i_max * i_min -1)
