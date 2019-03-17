points = list(map(int,input().split()))
pre = 0
ans = 0
for i in points:
    if i==2:
        ans+=pre*2+2
        pre+=1
    else:
        pre=0
        ans+=i

print(ans)
