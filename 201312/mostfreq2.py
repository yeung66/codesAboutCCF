n = int(input())
nums = list(map(int,input().split()[:n]))

count = [0 for _ in range(10001)]

for i in nums:
    count[i]+=1

maxi,index = count[1],1
for i in range(1,10001):
    if count[i]>maxi:
        maxi,index = count[i],i
print(index)
