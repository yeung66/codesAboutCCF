n = int(input())
nums = list(map(int,input().split()[:n]))

hashmap = {}
for i in nums:
    if i in hashmap:hashmap[i]+=1
    else:hashmap[i]=1

count = [(k,v) for k,v in hashmap.items()]
# print(count)
for i in range(len(count)-1):
    for j in range(i+1,len(count)):
        if count[i][1]<count[j][1] or (count[i][1]==count[j][1] and count[i][0]>count[j][0]):
            count[i],count[j]=count[j],count[i]

for k,v in count:
    print(k,v)