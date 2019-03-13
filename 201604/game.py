n,m,t = list(map(int,input().split()))
danger = {}
visited = [[[False for _ in range(302)] for _ in range(m+1)]for _ in range(n+1)]

for _ in range(t):
    r,c,a,b = list(map(int,input().split()))
    for i in range(a,b+1):
        visited[r][c][i]=True

##print(danger)
directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
from queue import Queue
def bfs():
    q = Queue()
    q.put((1,1,0))
    while not q.empty():
        pos = q.get()
        x,y,t = pos
        if x==n and y==m:return t
        for dx,dy in directions:
            nx,ny,nt = x+dx,y+dy,t+1
            if 1<=nx<=n and 1<=ny<=m and not visited[nx][ny][nt]:
                q.put((nx,ny,nt))
                visited[nx][ny][nt]=True

                
print(bfs())
