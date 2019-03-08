n = int(input())
nums = list(map(int,input().split()[:n]))


down = False if n>1 and nums[0]<nums[1] else True
count = 0
for i in range(n-1):
    # print(count)
    if down and nums[i]<nums[i+1]:
        down = False
        count+=1
    elif not down and nums[i]>nums[i+1]:
        down = True
        count+=1

print(count)