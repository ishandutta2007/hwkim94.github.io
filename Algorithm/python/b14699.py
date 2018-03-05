import sys

n, m = map(int, sys.stdin.readline().split())
height = [0] + list(map(int, sys.stdin.readline().split()))

graph = list(map(lambda x : x.strip(), sys.stdin.readlines()))
direction = [False] * (n+1)
path_num = [0] * (n+1)
result = [0] * (n+1)

for direc in graph :
    s, f = map(int, direc.split())
    
    if height[s] > height[f] :
        s, f = f, s
    
    path_num[s] += 1

    if direction[f] :
        direction[f].append(s)
    else :
        direction[f] = [s]

lst = [x for x in range(1, n+1) if not path_num[x]]
for idx in lst :
    result[idx] = 1
    
while lst :
    start = lst.pop(0)
    
    if not direction[start] :
        continue
    
    for node in direction[start] :

        path_num[node] -= 1

        if result[node] < result[start] + 1 :      
            result[node] = result[start] +1 

        if not path_num[node] :
            lst.append(node)

sys.stdout.write("\n".join(map(str, result[1:])))
        
