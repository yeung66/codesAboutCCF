n = int(input())
nums = list(map(int,input().split(' ')[:n]))
nums.sort()
i,j = 0,len(nums)-1
count = 0
while i<j:
    if nums[i]+nums[j]==0:
        count+=1
        i,j=i+1,j-1
    elif nums[i]+nums[j]<0:
        i+=1
    else:
        j-=1
print(count)