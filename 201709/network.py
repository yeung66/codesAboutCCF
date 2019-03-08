M,N = list(map(int,input().split()))
connect = [[0 for _ in range(M+1)] for _ in range(M+1)]

edges = [set() for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,M+1):
        if i==j:connect[i][j]=1

for _ in range(N):
    u,v = list(map(int,input().split()))
    edges[u].add(v)

##print(edges[1][1:M+1])
##print(edges[2][1:M+1])
##print(edges[3][1:M+1])

visited = [False for _ in range(M+1)]
def dfs(start,i):
    visited[i] = True
    for j in edges[i]:
##        print(i,j,not visited[j],edges[i][j])
        if not visited[j]:
            connect[start][j]=connect[j][start]=1
            dfs(start,j)


for i in range(1,M+1):
    visited = [False for _ in range(M+1)]
    dfs(i,i)
##print(connect[1][1:N+1])

count=0
for c in connect:
    if sum(c)==M:count+=1
print(count)
