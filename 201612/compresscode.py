n = int(input())
nodes = [0]+list(map(int,input().split()))
from math import inf as INF
ans = [[INF for _ in range(n+2)] for _ in range(n+2)]
sums = [0]+[sum(nodes[1:i+1]) for i in range(1,n+1)]
p = [[0 for _ in range(n+1)] for _ in range(n+1)]
     
##print(nodes)
##print(sums)
for i in range(1,n+1):
     ans[i][i]=0
     p[i][i]=i

for ll in range(2,n+1):
    for i in range(1,n-ll+1+1):
        j=i+ll-1
        for k in range(p[i][j-1],p[i+1][j]+1):
            val = ans[i][k]+ans[k+1][j]+sums[j]-sums[i-1]
            if val<ans[i][j]:
                ans[i][j]=val
                p[i][j]=k

##print(ans)
print(ans[1][n])
