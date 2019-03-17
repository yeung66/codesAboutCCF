n,k = list(map(int,input().split()))
keys = [i for i in range(1,n+1)]
event = []

for _ in range(k):
    no,start,l = list(map(int,input().split()))
    borrow = (start,1,no)
    back = (start+l,0,no)
    event.append(borrow)
    event.append(back)

event.sort()
##print(event)
for e in event:
    if e[1]==0:
        for i in range(n):
            if keys[i]==0:
                keys[i]=e[2]
                break
    else:
        index = keys.index(e[2])
        keys[index]=0

print(' '.join(map(str,keys)))
