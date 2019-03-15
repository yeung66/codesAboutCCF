n,m = list(map(int,input().split()))
edges = [[False for _ in range(n+1)] for _ in range(n+1)]
visited = [[False for _ in range(n+1)] for _ in range(n+1)]
flag = False
# 并查集 检查连通性
v = [i for i in range(n+1)]
def find(x):
    if x==v[x]:return x
    else:
        v[x] = find(v[x])
        return v[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:return False
    else:
        v[x] = y
        return True

for _ in range(m):
    u,j = list(map(int,input().split()))
    edges[u][j]=edges[j][u]=True
    union(u,j)

for i in range(2,n):
    root = find(1)
    if find(i)!= root:
        flag=True

count=0
for i in range(1,n+1):
    e = [j for j in edges[i] if j]
    if len(e)%2==1:
        count+=1

if not (count==0 or count==2 and len([j for j in edges[1] if j])%2==1):
    flag=True

ans = []
end = False
path = []
def dfs(i):
####    flag = False
    for j in range(1,n+1):
        if edges[i][j] and not visited[i][j]:
##            flag=True
            visited[i][j]=visited[j][i]=True
            dfs(j)
    path.append(i)
if flag:
    print(-1)
else:
    dfs(1)
    print(' '.join(map(str,path[::-1])))
