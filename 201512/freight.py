n,m = list(map(int,input().split()))
edges = [[False for _ in range(n+1)] for _ in range(n+1)]
visited = {}

for _ in range(m):
    u,v = list(map(int,input().split()))
    edges[u][v]=edges[v][u]=True
    visited[(u,v)]=visited[(v,u)]=0

ans = []
end = False

def dfs(i,pre=[]):
####    flag = False
    for j in range(1,n+1):
        if edges[i][j] and not visited[(i,j)]:
##            flag=True
            visited[(i,j)]=visited[(j,i)]=1
            if close():
                print(' '.join(map(str,pre+[i,j])))
                exit(0)
            else:dfs(j,pre+[i])
            visited[(i,j)]=visited[(j,i)]=0
##    if not flag and clo
    

def close():
    result = [visited[k] for k in visited]
    return sum(result)==2*m

dfs(1)
print(-1)
