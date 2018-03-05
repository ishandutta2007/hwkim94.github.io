#문제의 예제코드를 보면, 뒤에도 공백이 있음을 알 수 있음. 주의.
num = int(input())

blank = " "
nblank = num-1

dic = {nblank : "*", nblank-1 : "* *", nblank-2 : "*****"}
length = 5
flag = 3
count = 0

for idx in range(nblank, -1, -1) :
    if idx in dic :
        pass
    
    else :
        temp = dic[nblank-count] 
        dic[idx] = temp + (blank * (length -count*2)) + temp

        count += 1

    if count >= flag:
        count = 0
        length = len(dic[min(dic.keys())])
        flag = len(dic)

for idx in range(nblank, -1, -1) :
    print(blank * idx, end="")
    print(dic[idx], end = "")
    print(blank * idx)

            
    
        
