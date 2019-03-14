##n,m = list(map(int,input().split()))
##
##class Node:
##    def __init__(self):
##        self.children=[]
##        self.level = 0
##        self.no = 0
##        self.type = 0
##        self.parent = None
##
##routers = [Node() for _ in range(n+1)]
##computers = [Node() for _ in range(n+1)]
##
##routers[1].level = 1
##routers[1].no = 1
##
##parents = list(map(int,input().split()[:n-1]))
##
##for i,p in enumerate(parents):
##    this = routers[i+1+1]
##    parent = routers[p]
##    this.no=i+1+1
##    this.level=parent.level+1
##    this.parent=parent
##    parent.children.append(this)
##
##parents = list(map(int,input().split()[:m]))
##for i,p in enumerate(parents):
##    this = computers[i+1]
##    this.type=1
##    parent = routers[p]
##    this.no=i+n+1
##    this.level=parent.level+1
##    this.parent=parent
##    parent.children.append(this)
##
##leafs = set([i.no for i in routers[1:] if len(i.children)==0])
####print(leafs)
##ans = 0
##count=0
##max_node = None
####visited = [False for _ in range(n+m+1)]
##def dfs(node,count,visited):
##    global ans,max_node
##    if visited[node.no]:return
##    visited[node.no]=True
####    print(node.no)
##    if node.type==1 or node.no in leafs:
####        print(count)
##        if count>ans:
##            ans = count
##            max_node = node
##    for c in node.children:
##        dfs(c,count+1,visited)
##    if node.parent:dfs(node.parent,count+1,visited)
##
##def bfs(s):
##    
##
####for i in leafs:
####    visited = [False for _ in range(n+m+1)]
####    dfs(routers[i],0,visited)
####
####for i in computers[1:]:
####    visited = [False for _ in range(n+m+1)]
####    dfs(i,0,visited)
##
##dfs(computers[1],0,[False for _ in range(n+m+1)])
##dfs(max_node,0,[False for _ in range(n+m+1)])
##
##print(ans)


## 可将树当作无向图处理
n,m = list(map(int,input().split()))
graph = [[]for _ in range(n+m+1)]

routers = list(map(int,input().split()[:n-1]))
for i in range(n-1):
    u,v = i+2,routers[i]
    graph[u].append(v)
    graph[v].append(u)

coms = list(map(int,input().split()[:m]))
for i in range(m):
    u,v = n+i+1,coms[i]
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(n+m+1)]
##print(graph)
def bfs(i):
    queue = []
    queue.append(i)
    count = 0
    node = 0
    visited[i]=True
    while queue:
        node = queue.pop(0)
##        print(node)
##        visited[node]=True
        for e in graph[node]:
            if not visited[e]:
                queue.append(e)
                visited[e]=True
    return node

dis = [0 for _ in range(n+m+1)]
def bfs_count(i):
    queue = []
    queue.append(i)
    count = 0
    node = 0
    visited[i]=True
    while queue:
        
        node = queue.pop(0)
##        print(node)
        for e in graph[node]:
            if not visited[e]:
                queue.append(e)
                dis[e] = dis[node]+1
                visited[e]=True
    return dis[node]
    
start = bfs(1)
visited = [False for _ in range(n+m+1)]
print(bfs_count(start))
        
