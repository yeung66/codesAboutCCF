n,k = list(map(int,input().split()))
children = [i for i in range(1,n+1)]
index = -1
cur = 0
while len(children)>1:
    cur+=1
    index=(index+1)%len(children)
    if cur%k==0 or cur%10==k:
        children.pop(index)
        index=(index-1)%len(children)

print(children[0])
    
