import math
n,m,k,r = tuple(map(int,input().split(' ')))
points = []

for _ in range(n+m):
    points.append(list(map(int,input().split(' '))))

neigh = [[0 for _ in range(n+m)] for _ in range(n+m)]
distance = lambda x,y:(x[0]-y[0])**2+(x[1]-y[1])**2

for i in range(n+m):
    for j in range(i+1,n+m):
        if distance(points[i],points[j])<=r*r:neigh[i][j]=neigh[j][i]=1

d = [[math.inf for _ in range(k+1)]for _ in range(n+m)]
visit = [[0 for _ in range(k+1)]for _ in range(n+m)]
queue = [(0,0)]

# spfa算法
d[0][0] = 0
visit[0][0] = 1
while len(queue)!=0:
    p = queue[0]
    queue = queue[1:]
    visit[p[0]][p[1]] = 0
    # print(p)
    for i in range(n+m):
        if neigh[p[0]][i]:
            # print(i)
            temp = [i,p[1]]
            # print(temp[0])
            if i>=n:temp[1]+=1
            if temp[1]<=k and d[temp[0]][temp[1]]>d[p[0]][p[1]]+1:
                d[temp[0]][temp[1]] = d[p[0]][p[1]]+1
                if visit[temp[0]][temp[1]]==0:
                    visit[temp[0]][temp[1]]=1
                    queue.append(temp)
                
ans = math.inf
for i in d[1]:
    ans = min(i,ans)


print(ans-1)
