n,k = tuple(map(int,input().split()))

cakes = tuple(map(int,input().split()))

count = 0
temp = 0

for i in cakes:
    if temp==0:count+=1
    temp+=i
    if temp>=k:temp=0

print(count)