from math import inf as INF

n,m=list(map(int,input().split()))
edges = [[INF for _ in range(n+1)]for _ in range(n+1)]

for _ in range(m):
    u,v,t = list(map(int,input().split()))
    edges[u][v]=edges[v][u]=t


##ans = INF
##used = set()
##visited = [False for _ in range(n+1)]
##
##def DFS(i):
##    global used,ans,visited
####    print(i,ans)
##    if i==n:
####        print(used)
##        new_ans = max(used)
##        if new_ans<ans:ans = new_ans
##        return
##    else:
##        visited[i]=True
##        for j in range(1,n+1):
##            if edges[i][j]<INF and not visited[j]:
##                if edges[i][j]>=ans:continue
##                flag = False
##                if edges[i][j] not in used:
##                    used.add(edges[i][j])
##                    flag=True
##                DFS(j)
##                if flag:used.remove(edges[i][j])
##        visited[i]=False
##
##DFS(1)
##print(ans)
        
visited = [False for _ in range(n+1)]
##ans = [INF for _ in range(n+1)]
##def spfa():
##    queue = [1,]
##    visited[1]=True
##    ans[1]=0
##    while queue:
##        i = queue.pop(0)
##        visited[i]=False
##        for j in range(1,n+1):
##            if edges[i][j]<INF:
##                new = max(edges[i][j],ans[i])
##                if new<ans[j]:
##                    ans[j]=new
##                    if not visited[j]:
##                        queue.append(j)
##                        visited[j]=True
##
##spfa()
##
from queue import PriorityQueue
def dj():
    pq = PriorityQueue()
    pq.put((0,1))
##    count=0
    while not pq.empty():
        cost,i = pq.get()
        if visited[i]:continue
        visited[i]=True
        if i==n:return cost
##        if count==n:return cost
        for j in range(1,n+1):
            if edges[i][j]<INF:
                pq.put((max(cost,edges[i][j]),j))

print(dj())
                    
                
                
    
