n = int(input())
nums = list(map(int,input().split()[:n]))

nums.sort()
flag=False
for i in set(nums):
    less,more=0,0
    for j in nums:
        if j<i:less+=1
        elif j>i:more+=1
    
    if less==more:
        print(i)
        flag=True
        break

if not flag:print(-1)