import sys

n,m = map(int, input().split())
lst = list(map(lambda x : x.strip(), sys.stdin.readlines()))

distance = [False] + [list([0]+[float('inf')]*n) for _ in range(n)] 
for elt in lst :
    a,b = map(int, elt.split())
    distance[a][b], distance[b][a] =1,1

for idx in range(1, n+1) :
    for idx2 in range(1, n+1) :
        for idx3 in range(1, n+1) :
            if distance[idx2][idx3] > distance[idx2][idx] + distance[idx][idx3] :
                distance[idx2][idx3] = distance[idx2][idx] + distance[idx][idx3]

tot = float('inf')
people = float('inf')
for idx in range(1, n+1) : 
    temp = sum(distance[idx])

    if temp < tot :
        people = idx
        tot = temp

print(people)
