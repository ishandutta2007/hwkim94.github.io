import sys
sys.setrecursionlimit(100000)

a, b, c = map(int, input().split())
lst = list(map(lambda x: x.strip(), sys.stdin.readlines()))
finish_dfs = set([])
finish_bfs = set([])
dfs_way = []
bfs_way =[]
dic= {}

for line in lst :
    e,f = map(int, line.split())
    
    if e in dic :
        dic[e].add(f)
    else :
        dic[e] = set([f])

    if f in dic :
        dic[f].add(e)
    else :
        dic[f] = set([e])

def dfs(val) :
    dfs_way.append(val)
    finish_dfs.add(val)
    
    temp=sorted(list(dic[val]))
    [dfs(x) for x in temp if (x not in finish_dfs)]

def bfs(val) :
    lst = [val]
    
    while lst :
        finish_bfs.update(lst)
        bfs_way.extend(lst)

        temp = list(lst)
        lst = []

        for idx in temp :
            lst.extend(sorted([x for x in dic[idx] if (x not in lst) and (x not in finish_bfs) and (x != idx)]))

if c in dic :  
    dfs(c)
    bfs(c)
    print(" ".join(map(str, dfs_way)))
    print(" ".join(map(str, bfs_way)))
else :
    print(c)
    print(c)
