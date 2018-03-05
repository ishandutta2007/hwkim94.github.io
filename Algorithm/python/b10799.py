stick = input().replace("()", ".").strip(".")
num = 0
total = 0

for idx in stick :
    if idx == "(" :
        num += 1
    elif idx == "." :
        total += num
    elif idx == ")" :
        num -= 1
        total += 1

print(total)
        


 
        

            
        
