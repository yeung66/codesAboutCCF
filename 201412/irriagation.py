n,m = list(map(int,input().split()))
edges = [{}for _ in range(n+1)]

for _ in range(m):
    u,v,c = list(map(int,input().split()))
    if v in edges[u]:c=min(edges[u][v],c)
    edges[u][v]=c
    edges[v][u]=c
from math import inf as INF
visited = [False for _ in range(n+1)]


from queue import PriorityQueue
pq = PriorityQueue()

pq.put((0,1))
ans,count = 0,0
while not pq.empty():
    c,front = pq.get()
    if visited[front]:continue
    visited[front]=True
    ans+=c
    count+=1
    for e,cost in edges[front].items():
        if not visited[e]:            
            pq.put((cost,e))
    if count==n:break

##print(dp[1:])
print(ans)
      
