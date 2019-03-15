n,m,k,d=list(map(int,input().split()))

from math import inf as INF
branchs = []
dp = [[INF for _ in range(n+1)]for _ in range(n+1)]
for _ in range(m):
    branchs.append(tuple(map(int,input().split())))
    
directions = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs(start,visited):
    queue = []
    queue.extend(start)
    while queue:
        i,j = queue.pop(0)
##        print(i,j)
##        if visited[i][j]:continue
        for dx,dy in directions:
            nx,ny = i+dx,j+dy
            if 1<=nx<=n and 1<=ny<=n and not visited[nx][ny]:
                visited[nx][ny]=True
                dp[nx][ny]=min(dp[nx][ny],dp[i][j]+1)
                queue.append((nx,ny))

visited = [[False for _ in range(n+1)]for _ in range(n+1)]
guests = []
for _ in range(k):
    guests.append(tuple(map(int,input().split())))
danger = []
for _ in range(d):
    x,y = list(map(int,input().split()))
    visited[x][y]=True

for bx,by in branchs:
    visited[bx][by]=True
    dp[bx][by]=0
bfs(branchs,visited)

##for i in range(1,n+1):print(dp[i][1:])
ans = 0
for gx,gy,gn in guests:
    ans+=dp[gx][gy]*gn

print(ans)
            
