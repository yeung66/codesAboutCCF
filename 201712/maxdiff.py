n = int(input())
nums = list(map(int,input().split()[:n]))
nums.sort()
nums = [abs(nums[i]-nums[i+1]) for i in range(n-1)]
##print(nums)
print(min(nums))
