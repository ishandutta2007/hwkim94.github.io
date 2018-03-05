from collections import defaultdict
import heapq

def dijkstra(network, n) :
    start = 1
    
    dic = dict(network)
    distance = defaultdict(lambda : float("inf"))
    distance[start] = 0
    
    visited = [False]*(n+1)
    visited[start] = True
    visited[0] = True

    lst = []
    result = []

    while not all(visited) :
        for node, time in dic[start] :
            if not visited[node] :
                test = min(distance[node], time + distance[start])

                if distance[node] > test :
                    distance[node] = test
                    heapq.heappush(lst, (distance[node], node, start))
                
                
        while lst :
            if not visited[lst[0][1]] :
                start = lst[0][1]
                result.append((start, lst[0][2]))
                visited[start] = True
                heapq.heappop(lst)
                break
            
            else :
                heapq.heappop(lst)

    return result
            

#--main--
network = defaultdict(lambda : [])
n, m = map(int, input().split())
for _ in range(m) :
    a, b, c = map(int, input().split())
    
    if a == b :
        continue
    
    network[a].append((b, c))
    network[b].append((a, c))

result = dijkstra(network, n)
print(len(result))
[print(x[0], x[1]) for x in result]

