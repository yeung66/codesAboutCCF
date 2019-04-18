n = int(input())

nums = list(map(int,input().split()[:n]))

if n%2==1:mid = nums[n//2]
else:
    mid=(nums[n//2-1]+nums[n//2])/2
    if mid==int(mid):mid=int(mid)

maxi,mini = (nums[0],nums[n-1]) if nums[0]>nums[n-1] else (nums[n-1],nums[0])

print(maxi,mid,mini)
