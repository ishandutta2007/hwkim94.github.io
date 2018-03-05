import sys
sys.setrecursionlimit(1000000)

#--선언부--
def calculate(lst, check_lst) :
    c_row, c_col, func = check_lst[0], check_lst[1], check_lst[2].strip("=").split("+")
    row, col, tot = 0,0,0

    for elt in func :
        if elt[0] in "-0123456789" :
            tot += int(elt)
            continue
        
        for idx, types in enumerate(elt) :
            if types in "01234567890" :
                                    
                temp = elt[:idx]
                row = int(elt[idx:])-1
                    
                if len(temp) == 3 :
                    col = (ord(temp[0])-64)*26**2 + (ord(temp[1])-64)*26 + (ord(temp[2])-64)
                elif len(temp) == 2 :
                    col = (ord(temp[0])-64)*26 + (ord(temp[1])-64)
                elif len(temp) == 1 :
                    col = (ord(temp[0])-64)
                    
                break

        value = lst[row][col]
        if type(value) != int :
            value = calculate(lst, (row,col,value))
            lst[row][col] = value
            
        tot += value

    return tot
                    
#--main--
test = int(input())

for _ in range(test) :
    col, row = map(int, sys.stdin.readline().split())
    shit = {}
    check = []

    row_num = 0
    for __ in range(row) :
        line = sys.stdin.readline().split()
        result = [False]
        
        for elt in line :
            if elt[0] == "=" :
                check.append((row_num,len(result),elt))
                result.append(elt)
                
            else :
                result.append(int(elt))
        
        shit[row_num] = result
        row_num += 1

    for val in check :
        shit[val[0]][val[1]] = calculate(shit, val)

    for temp in sorted(list(shit.items()), key = lambda x : x[0]) :
        r_row = temp[1]
        print(" ".join(list(map(str, r_row[1:]))))
    
