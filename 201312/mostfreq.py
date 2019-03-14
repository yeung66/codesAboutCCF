n = int(input())
nums = list(map(int,input().split(' ')[:n]))
count = {}
for n in nums:
    if n in count:count[n]+=1
    else:count[n]=1

result = [(v,k) for k,v in count.items()]
result.sort()
m = max(result,key=lambda x:x[0])
for i in result:
    if i[0]==m[0]:
        print(i[1])
        break