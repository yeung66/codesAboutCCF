from math import inf as INF
MAX = 1000
dl,xl = [[INF for _ in range(MAX)] for _ in range(MAX)],[[INF for _ in range(MAX)] for _ in range(MAX)]

dist1,dist2 = [INF for _ in range(MAX)],[INF for _ in range(MAX)]

n,m = list(map(int,input().split()))

for _ in range(m):
    t,u,v,c = list(map(int,input().split()))
    if t and xl[u][v]>c:
        xl[u][v]=xl[v][u]=c
    elif t==0 and dl[u][v]>c:
        dl[u][v]=dl[v][u]=c


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if xl[i][j]>xl[i][k]+xl[k][j] and xl[i][k]<INF and xl[k][j]<INF:
                xl[i][j]=xl[i][k]+xl[k][j]

# print(xl[1:n+1])

from queue import Queue

visited = [False for _ in range(n+1)]
q = Queue()
q.put(1)
dist1[1]=dist2[1]=0
while not q.empty():
    node = q.get()
    # print(node)
    visited[node]=0
    for i in range(1,n+1):
        if i==node:continue
        v = dl[node][i]
        # print(v)
        if dist1[i]>dist1[node]+v:
            dist1[i]=dist1[node]+v
            if not visited[i]:
                visited[i]=True
                q.put(i)
        if dist1[i]>dist2[node]+v:
            dist1[i]=dist2[node]+v
            if not visited[i]:
                visited[i]=True
                q.put(i)
        if xl[node][i]<INF:
            if dist2[i]>dist1[node]+xl[node][i]**2:
                dist2[i]=dist1[node]+xl[node][i]**2
                if visited[i]:continue
                visited[i]=True
                q.put(i)
print(dist1[1:n+1])
print(dist2[1:n+1],'\n')
print(min(dist1[n],dist2[n]))

