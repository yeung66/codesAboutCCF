n = int(input())
nums = list(map(int,input().split()[:n]))
nums.sort()
ans = 0
for i in range(n-1):
    if -1<=nums[i]-nums[i+1]<=1:ans+=1

print(ans)
