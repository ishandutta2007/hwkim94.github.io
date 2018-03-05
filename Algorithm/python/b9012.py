num = int(input())
for idx in range(num):
    a = input()
    while "()" in a :
        a = a.replace("()", "")

    if a == "" :
        print("YES")
    else :
        print("NO")
