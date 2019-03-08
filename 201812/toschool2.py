r,y,g = map(int,input().split(' '))
n = int(input())
ans = 0
for _ in range(n):
    k,t = map(int,input().split(' '))
    if k==0:ans+=t
    else:
        time_sign = r-t if k==1 else r+g-t if k==3 else r+y+g-t
        time_sign+=ans
        time_sign %= r+y+g
        if time_sign<r:
            ans+=r-time_sign
        elif time_sign>=r+g:
            ans+=r+y+g-time_sign+r

print(ans)