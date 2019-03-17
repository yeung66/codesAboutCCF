n,L,t = list(map(int,input().split()))
pos = list(map(int,input().split()[:n]))

direction = [1 for i in range(n)]

for i in range(t):
    now = {}
    for p in range(n):
        pos[p]+=direction[p]
        if pos[p] in now:
            direction[p]=-direction[p]
            direction[now[pos[p]]]=-direction[now[pos[p]]]
        else:
            now[pos[p]]=p
        if pos[p]==0 or pos[p]==L:
            direction[p]=-direction[p]

print(' '.join(map(str,pos)))
        
