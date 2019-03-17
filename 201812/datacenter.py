from  queue import PriorityQueue as PQueue

MAX = 100000

##def prim(start,graph):
##    t = {}
##    n = len(graph)
##    visited = [False for _ in range(n)]
##    parents = [-1 for _ in range(n)]
##    edges = PQueue(MAX)
##    edges.put([0,start,-1])
##    while len(t)<n:
##        mini_edge = edges.get()
##        # print(mini_edge)
##        while visited[mini_edge[1]]:
##            mini_edge = edges.get()
##        # print(mini_edge)
##        mini_node = mini_edge[1]
##        visited[mini_node]=True
##        t[mini_node]=mini_edge[0]
##        parents[mini_node]=mini_edge[2]
##
##        for k,v in graph[mini_node]:
##            if visited[v]:continue
##            edges.put([k,v,mini_node])
##
##    return t



n = int(input())
m = int(input())
start = int(input())
from math import inf as INF
edges = [[] for _ in range(n+1)]

def prim(start):
    pq = PQueue()
    pq.put((0,start))
    cost = [INF for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    count = 0
##    cost[1]=0
    while not pq.empty():
        c,node = pq.get()
        if visited[node]:continue
        visited[node]=True
        cost[node]=c
        count+=1
        if count==n:
##            print(cost[1:])
            return max(cost[1:])
        for e in edges[node]:
            if not visited[e[1]]:
                pq.put((e[0],e[1]))
                
            
for _ in range(m):
    v,u,t = list(map(int,input().split()))
    edges[v].append((t,u))
    edges[u].append((t,v))

t = prim(start)


print(t)
