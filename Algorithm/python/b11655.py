string = input()
result = ""
for idx in string :
    if (48 <= ord(idx) <=57) or (idx == " ") :
        result += idx
        continue
        
    elif (65 <= ord(idx) <=90) and ord(idx) +13 > 90 :
        result += chr(ord(idx) + 13 -26 )
    elif (97<=ord(idx) <= 122) and ord(idx) +13 >122 :
        result += chr(ord(idx) + 13 -26 )
    else :
        result += chr(ord(idx) + 13)

print(result)
