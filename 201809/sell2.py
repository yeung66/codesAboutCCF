t = int(input())

a = [1]+list(map(int,input().split()[:t]))
b = [0 for i in range(t+1)]
visited = set()
ans = []
def dfs(n,x,y):
    if (n,x,y) in visited:return
    visited.add((n,x,y))
    if n==t-1:
        if (3*a[n]-x)//2==a[n+1]:
            b[n+1] = 3*a[n]-x-y
        elif (3*a[n]-x+1)//2==a[n+1]:
            b[n+1] = 3*a[n]-x-y+1
        elif (3*a[n]-x+2)//2==a[n+1]:
            b[n+1] = 3*a[n]-x-y+2
        else:
            return
        if b[n+1]<1:return
        print(' '.join(map(str,b[1:])))
        exit(0)
        # print(b[1:])
        return
    else:
        for i in range(3):
            b[n+1]=3*a[n]-x-y+i
            if b[n+1]>=1:
                dfs(n+1,y,b[n+1])

for i in range(1,2*a[1]+1):
    b[1]=i
    b[2]=2*a[1]-b[1]
    dfs(2,i,b[2])
    b[1]=i
    b[2]=2*a[1]-b[1]+1
    dfs(2,i,b[2])

# ans.sort()
print(ans)
print(' '.join(map(str,ans[0])))
