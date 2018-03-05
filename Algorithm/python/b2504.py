def calculator(line) :
    
    # 맞는 괄호열인지 확인
    num = len(line)//2 + 1
    temp = line
    for idx in range(num) :
        temp = temp.replace("()", "").replace("[]", "")
        
    if temp != "" :
        return 0

    # 연산
    if line[0] == "(" :
        result = "2"
        flag = "("
        
    else :
        result = "3"
        flag = "["
    
    for idx in line[1:] :
        if idx == "(" :
            if flag in ("(", "["):
                result = result + "*(2"    
            else :
                result = result + "+2"

        elif idx == "[" :
            if flag in ("(", "["):
                result = result + "*(3"
            else :
                result = result + "+3"

        else  :
            if flag in (")", "]") :
                result = result + ")"

        flag = idx
            
    return eval(result)
    
print(calculator(input()))
