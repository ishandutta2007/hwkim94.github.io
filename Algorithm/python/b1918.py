def calculator(line) :
    #후위표기식 만들기, 괄호를 만들어주는 함수가 필요
    result = ""
    temp1 = []
    temp2 = []
    number = 0
    index = 0
    
    for idx in line :
        if idx.isalpha() :
            temp1.append(idx)
            continue

        if idx == "(" :
            number += 1
            index -= 1
            continue
            
        if idx == ")" :
            number -= 1
            index += 1

            if number == 0 :
                temp1.extend(temp2)
                result = result + "".join(temp1)
                temp1 = []
                temp2 = []
                number = 0
                index = 0
            
            continue

        if idx in "+-*/" :
            temp2.insert(index, idx)
            continue

    temp1.extend(temp2)
    result = result + "".join(temp1)
        
    return result

#위의 방법은 괄호를 만드는 방법이 없어서 불가
def calculator2(line) :
    result = []
    temp = []

    for idx in line :
        if idx.isalpha() :
            result.append(idx)
            
        elif idx == "(" :
            temp.append(idx)
            
        elif idx == ")" :
            while temp and (temp[-1] != "(") :
                result.append(temp.pop())
            temp.pop()
            
        elif idx in "+-" :  
            while temp and (temp[-1] != "("):
                result.append(temp.pop())
            temp.append(idx)

        elif idx in "/*" :
            while temp and (temp[-1] not in "+-("):
                result.append(temp.pop())
            temp.append(idx)

    while temp :
        result.append(temp.pop())
        
    return "".join(result)
    

print(calculator2(input()))




