n = int(input())
H,W = [],[]
for _ in range(n):
    H.append(tuple(map(int,input().split())))

for _ in range(n):
    W.append(tuple(map(int,input().split())))
# H.sort()
# W.sort()
ans = 0
i,j = 0,0
while i<n and j<n:
    h1,h2 = H[i]
    w1,w2 = W[j]
    if h1<=w1<=h2:
        if w2>h2:
            ans+=h2-w1
            i+=1
        else:
            ans+=w2-w1
            j+=1
    elif w1<=h1<=w2:
        if h2>w2:
            ans+=w2-h1
            j+=1
        else:
            ans+=h2-h1
            i+=1
    elif h2<w1:i+=1
    else:j+=1

print(ans)