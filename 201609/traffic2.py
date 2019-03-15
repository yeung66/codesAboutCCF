n,m = list(map(int,input().split()))
edges = [{}for _ in range(n+1)]

for _ in range(m):
    u,v,t = list(map(int,input().split()))
    if v in edges[u]:t=min(t,edges[u][v])
    edges[u][v]=t
    edges[v][u]=t

from math import inf as INF
dp = [INF for _ in range(n+1)]
p = [INF for _ in range(n+1)]
dp[1] = 0
p[1] = 0

from queue import Queue
q = Queue()
q.put(1)
inqueue = [False for _ in range(n+1)]
while not q.empty():
    front = q.get()
    inqueue[front]=False
    for e,cost in edges[front].items():
        if dp[front]+cost<dp[e]:
            dp[e]=dp[front]+cost
            p[e]=cost
            if not inqueue[e]:
                q.put(e)
                inqueue[e]=True
        elif dp[front]+cost==dp[e]:
            p[e]=min(p[e],cost)
##print(dp[1:])
##print(p[1:])
print(sum(p[1:]))
