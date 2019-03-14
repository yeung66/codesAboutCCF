# import itertools

# n,m,k,r = list(map(int,input().split()))
# start = tuple(map(int,input().split()))
# end = tuple(map(int,input().split()))

# if start[0]<start[1]:x_direction=1
# else:x_direction=-1
# if start[1]<end[1]:y_direction=1
# else:y_direction=-1

# n_points_ori = []
# for _ in range(n-2):
#     n_points_ori.append(tuple(map(int,input().split())))
# # print(n_points)
# m_points = []
# for _ in range(m):
#     m_points.append(tuple(map(int,input().split())))

# def distance(x1,y1,x2,y2):
#         return ((x1-x2)**2+(y1-y2)**2)

# ans = 200
# for i in itertools.combinations(m_points,k):
#     n_points = n_points_ori[:]
#     n_points.extend(i)

#     n_points.sort(key=lambda x:(x[0]**2+x[1]**2))

    

#     dp = [200 for i in range(n+k)]
#     for i,(x,y) in enumerate(n_points):
#         if distance(start[0],start[1],x,y)<=r:dp[i]=1

#     for i,(x,y) in enumerate(n_points):
#         neigh = []
#         for j,(x1,y1) in enumerate(n_points):
#             if i==j:continue
#             elif distance(x,y,x1,y1)<=r:neigh.append(j)
#         # print(neigh)
#         if len(neigh)==0:continue
#         neigh = [dp[i]+1 for i in neigh]
#         # print(neigh)
#         dp[i] = min(dp[i],min(neigh))

#     for i,(x,y) in enumerate(n_points):
#         if distance(end[0],end[1],x,y)<=r:ans=min(ans,dp[i])

# # print(dp)
# print(ans)
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

d[0][0] = 0
visit[0][0] = 1
while len(queue)!=0:
    p = queue[0]
    queue = queue[1:]
    #visit[p[0]][p[1]] = 0
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