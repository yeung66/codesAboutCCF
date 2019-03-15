n = int(input())
nums = list(map(int,input().split()[:n]))

#分而治之
def find_largest(i,j):
    if i==j:return nums[i]
    elif j-i==1:return min(nums[i],nums[j])*2
    else:
        min_index,min_value = i,nums[i]
        for k in range(i,j+1):
            if nums[k]<min_value:min_index,min_value=k,nums[k]
        whole = (j-i+1)*min_value
        if min_index==i:return max(whole,find_largest(i+1,j))
        elif min_index==j:return max(whole,find_largest(i,j-1))
        else:
            return max(whole,find_largest(i,min_index-1),find_largest(min_index+1,j))

print(find_largest(0,n-1))
