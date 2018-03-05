w,m,k = map(int,input().split())

while k != 0:
    if w//2 > m :
        if k >=2 :
            w -= 2
            k -= 2
        else :
            w -= 1
            k -= 1 
        
    elif w//2 < m :
        m -= 1
        k -= 1 
    
    elif w//2 == m  :
        if w%2 == 1 :
            w -= 1
            k -= 1
        
        if k>=3 :
            w -= 2
            m -= 1
            k -= 3
        else :
            w -= k
            k = 0
            m -= 1
            
         
print(min(w//2, m)) 
    
    
