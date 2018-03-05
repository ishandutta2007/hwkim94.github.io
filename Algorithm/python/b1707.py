# 이분 그래프임을 확인하기 위해서는 깊이가 1씩 깊어질때마다
# 색깔이 빨->파->빨->파 순으로 바뀌어야하는데
# 만약 같은 점을 두번 방문했을 때, 색이 다르면 이분그래프가 아니다.
import sys
sys.setrecursionlimit(100000)

def dfs(val, color, colorlst) :
    
    #해당 vertex의 색을 정해준다
    #color = (color +1) % 2 도 가능하지만, 더 느림
    if color == 1 :
        color = 0
    else :
        color =1

    #이전에 방문했던 점인지 확인한다.
    if colorlst[val]!= 3 :
        if colorlst[val] != color :
            return False
        else :
            return True

    #만약 아니라면, colorlst에 점의 색을 정해준다.
    colorlst[val] = color

    #지금은 아직 NO가 나오지 않았기 때문에 다른 점을 방문한다.
    for x in dic[val] :
        dfs_result = dfs(x,color, colorlst)
        
        #만약 NO가 발견되면 종료한다.
        if not dfs_result :
            return False
        
    return True

def binaryGraph(vertex) :
    colorlst = [3] * (vertex+1)
    
    for idx in range(1, vertex+1) :
        color = 0

        #탐색이 된 점은 제외
        if colorlst[idx] == 3 :
            result = dfs(idx, color, colorlst)  
        
            if not result:
                return "NO"
            
    return "YES"

#----main----

num = int(input())

for idx in range(num) :
    #defaultdict와 set의 조합으로 하는 것보다 list로 하는 것이 더 빠름
    #인덱스-1을 사용하는 것보다, 아예 index 0을 채워둘 빈칸을 만드는 것이 더 빠름
    a,b = map(int, sys.stdin.readline().split())
    dic = [[] for _ in range(a + 1)]

    for idx in range(b) :
        c, d = map(int, sys.stdin.readline().split())
        dic[c].append(d)
        dic[d].append(c)
        
    print(binaryGraph(a))
    

