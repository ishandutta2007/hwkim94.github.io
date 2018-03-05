import sys

word, string = list(map(lambda x: x.strip(),sys.stdin.readlines()))
step = len(word)


while True :
    idx = string.find(word)
    if idx == -1 :
        break
    
    string = string[:idx] + string[idx+step:]

    if string.find(word) == -1 :
        break
    
    idx = string.rfind(word)
    string = string[:idx] + string[idx+step:] 


print(string)

