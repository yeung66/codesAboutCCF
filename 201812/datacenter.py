from  queue import PriorityQueue as PQueue

MAX = 100000

def prim(start,graph):
    t = {}
    n = len(graph)
    visited = [False for _ in range(n)]
    parents = [-1 for _ in range(n)]
    edges = PQueue(MAX)
    edges.put([0,start,-1])
    while len(t)<n:
        mini_edge = edges.get()
        # print(mini_edge)
        while visited[mini_edge[1]]:
            mini_edge = edges.get()
        # print(mini_edge)
        mini_node = mini_edge[1]
        visited[mini_node]=True
        t[mini_node]=mini_edge[0]
        parents[mini_node]=mini_edge[2]

        for k,v in graph[mini_node]:
            if visited[v]:continue
            edges.put([k,v,mini_node])

    return t

n = int(input())
m = int(input())
start = int(input())

graph = [[] for _ in range(n)]

for _ in range(m):
    v,u,t = list(map(int,input().split()))
    v,u=v-1,u-1
    graph[v].append((t,u))
    graph[u].append((t,v))

t = prim(start-1,graph)

tcost = [t[i] for i in t]

print(max(tcost))