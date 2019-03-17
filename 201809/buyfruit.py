n = int(input())
nums = list(map(int,input().split()[:n]))
result = []

for i,num in enumerate(nums):
    if i==0:result.append(sum((nums[i],nums[i+1]))//2)
    elif i==n-1:result.append(sum((nums[i-1],nums[i]))//2)
    else:
        result.append(sum((num,nums[i-1],nums[i+1]))//3)

print(' '.join(map(str,result)))