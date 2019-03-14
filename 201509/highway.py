n,m = list(map(int,input().split()))

edges = [[]for _ in range(n+1)]

for _ in range(m):
    u,v = list(map(int,input().split()))
    edges[u].append(v)

##ans = [[0 for _ in range(n+1)]for _ in range(n+1)]

## DFS访问 每轮标记单向可达性 1s限制下10分
##def dfs(i,visited,start):
##    for j in edges[i]:
##        if not visited[i][j]:
##            visited[i][j]=True
##            ans[start][j]=1
##            dfs(j,visited,start)
##            visited[i][j]=False

## BFS 1s限制下50分
##def bfs(i,visited):
##    queue = [i]
##    while queue:
##        node = queue.pop(0)
##        for e in edges[node]:
##            if not visited[e]:
##                ans[i][e]=1
##                visited[e]=True
##                queue.append(e)

##for i in range(1,n+1):
##    visited = [False for _ in range(n+1)]
##    bfs(i,visited)
##
##count=0
##for i in range(1,n+1):
##    for j in range(i+1,n+1):
##        if ans[i][j] and ans[j][i]:count+=1

stack = []
instack = [False for _ in range(n+1)]
visited = [False for _ in range(n+1)]
DNF = [0 for _ in range(n+1)]
LOW = [0 for _ in range(n+1)]
ans=time = 0

# tarjan算法 找出图中强连通分量
def tarjan(i):
    global ans,time
    time+=1
    DNF[i]=LOW[i]=time
    stack.append(i)
    instack[i]=True
    visited[i]=True
    for j in edges[i]:
        if not visited[j]:
            tarjan(j)
            LOW[i]=min(LOW[j],LOW[i])
        elif instack[j]:
            LOW[i]=min(LOW[j],LOW[i])
    if DNF[i]==LOW[i]:
        count=0
        while True:
            node = stack.pop()
            instack[node]=False
            
            count+=1
            if node==i:break
        if count>1:ans+=(count-1)*count//2;

for i in range(1,n+1):
    if not visited[i]:tarjan(i)

print(ans)
