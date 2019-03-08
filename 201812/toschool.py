r,y,g = map(int,input().split(' '))
n = int(input())
ans = 0
for i in range(n):
    k,t = map(int,input().split(' '))
    if k<=1:ans+=t
    elif k==2:ans+=(t+r)

print(ans)