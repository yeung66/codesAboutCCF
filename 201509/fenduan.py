n = int(input())
nums = list(map(int,input().split(' ')[:n]))
count=1
for i,num in enumerate(nums):
    if i>0 and num!=nums[i-1]:count+=1

print(count)