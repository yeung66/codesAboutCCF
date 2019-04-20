n,m,kk=list(map(int,input().split()[:3]))
types = [0]+list(map(int,input().split()[:n]))

from math import inf

graph = [[inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):graph[i][i]=0

for _ in range(m):
    u,v,w=list(map(int,input().split()))
    if u==v:continue
    graph[u][v]=graph[v][u]=min(w,graph[u][v])


for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

##for i in range(1,n+1):
##    print(' '.join([str(j) for j in graph[i][1:]]))

for i in range(1,n+1):
    targets = [graph[i][j] for j in range(1,n+1) if types[j] and graph[i][j]<inf]
    targets.sort()
##    print(targets[:kk])
    if len(targets)<=kk:
        print(sum(targets))
    else:
        print(sum(targets[:kk]))
                             
    
    
