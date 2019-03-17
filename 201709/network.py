M,N = list(map(int,input().split()))
connect = [[0 for _ in range(M+1)] for _ in range(M+1)]

edges = [set() for _ in range(M+1)]

##for i in range(1,M+1):connect[i][i]=1

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

def bfs(start):
    q = [start,]
    visited[start]=True
    while q:
        i = q.pop(0)
        for j in edges[i]:
            if not visited[j]:
                connect[start][j]=connect[j][start]=1
                q.append(j)
                visited[j]=True


for i in range(1,M+1):
    visited = [False for _ in range(M+1)]
    bfs(i)
##print(connect[1][1:N+1])

count=0
##print(connect)
for c in connect:
    if sum(c)==M-1:count+=1
print(count)
