##n,m = list(map(int,input().split()))
##from math import inf as INF
##edges = [[INF for _ in range(n+1)] for _ in range(n+1)]
##
##for _ in range(m):
##    u,v,c = list(map(int,input().split()[:3]))
##    edges[u][v]=edges[v][u]=c
##
##class Node:
##    def __init__(self,p,n):
##        self.n=n
##        self.p=p
##
##    def __lt__(self,node):
##        return self.p<node.p
##
##from queue import PriorityQueue as PQueue
##pq = PQueue()
####pq = []
##dis = [INF for _ in range(n+1)]
##p = [INF for _ in range(n+1)]
##pq.put(Node(0,1))
##visited = [False for _ in range(n+1)]
##dis[1]=p[1]=p[0]=0
##while not pq.empty():
##    node = pq.get()
##    node = node.n
####    print(node)
##    if visited[node]:continue
##    visited[node]=True
##    for i in range(1,n+1):
##        if edges[node][i]<INF:
##            temp = edges[node][i]+dis[node]
##            if temp<dis[i]:
##                dis[i]=temp
##                p[i]=edges[node][i]
##                pq.put(Node(temp,i))
####                print(temp,i)
##            elif temp==dis[i]:
##                p[i]=min(p[i],edges[node][i])
####print(dis[1:])
######print(p[1:])
##print(sum(p))
##
##
from math import inf as INF
n,m = list(map(int,input().split()))
edges = [{} for _ in range(n+1)]

for _ in range(m):
    u,v,c = list(map(int,input().split()))
    edges[u][v]=c
    edges[v][u]=c

d = [INF for _ in range(n+1)]
visited = [False for _ in range(n+1)]
p = [0 for _ in range(n+1)]
d[1]=0
class Node:
    def __init__(self,d,u):
        self.d=d
        self.u=u

    def __lt__(self,node):
        return self.d>node.d
##print(edges)
from queue import PriorityQueue
pq = PriorityQueue()
pq.put(Node(0,1))
while not pq.empty():
    x = pq.get()
    u = x.u
    print(u)
    if visited[u]:continue
    visited[u]=True
    for k,v in edges[u].items():
        if d[k]>d[u]+v:
            d[k]=d[u]+v
            p[k]=v
            pq.put(Node(d[k],k))
        if d[k]==d[u]+v:                   
            p[k]=min(v,p[k])

print(sum(p[1:n+1]))
