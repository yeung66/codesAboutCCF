from math import inf as INF

n,m = list(map(int,input().split()))

dist1,dist2 = [INF for i in range(n+1)],[INF for i in range(n+1)]
xl,dl = [{} for _ in range(n+1)],[{} for _ in range(n+1)]

for _ in range(m):
    t,u,v,c = list(map(int,input().split()))
    if t:
        if v in xl[u]:xl[u][v]=xl[v][u]=min(c,xl[u][v])
        else:xl[u][v]=xl[v][u]=c
    else:
        if v in dl[u]:dl[u][v]=min(c,dl[u][v])
        else:dl[u][v]=dl[v][u]=c

# floyd算法 多源最短路径
for k in range(1,n+1):
    for i in range(1,n+1):
        pre = xl[i]
        if k in pre:
            nxt = xl[k]
            for j in nxt:
                if j not in pre:pre[j]=pre[k]+nxt[j]
                elif pre[j]>pre[k]+nxt[j]:
                    pre[j]=pre[k]+nxt[j]

##for x in range(1,n+1):
##    for k,v in xl[x].items():
##        if x in xl[k]:xl[x][k]=xl[k][x]=min(xl[x][k],xl[k][x])
##        else:xl[k][x]=xl[x][k]
### print(xl[1:])

from queue import Queue
inqueue = [False for _ in range(n+1)]

q = Queue()
q.put(1)
dist1[1]=dist2[1]=0
while not q.empty():
    node = q.get()
    inqueue[node]=False
    # print(node)
    for k,v in dl[node].items():
        flag = False
        if dist1[k]>dist1[node]+v:
            dist1[k]=dist1[node]+v
            flag=True
        if dist1[k]>dist2[node]+v:
            dist1[k]=dist2[node]+v
            flag=True
        if flag and not inqueue[k]:
            q.put(k)
    for k,v in xl[node].items():
        if dist2[k]>dist1[node]+v**2:
            dist2[k]=dist1[node]+v**2
            if inqueue[k]:continue
            inqueue[k]=True
            q.put(k)

# print(dist1[1:n+1])
# print(dist2[1:n+1],'\n')
print(min(dist1[n],dist2[n]))
