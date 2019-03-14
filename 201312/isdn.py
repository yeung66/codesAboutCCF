isbn = input()
nums = isbn.split('-')
total = 0
c = 1
for n in nums[:-1]:
    for i in n:
        total+=c*int(i)
        c+=1

ans = 'X' if total%11==10 else str(total%11)
if nums[-1]==ans:print('Right')
else:
    nums[-1]=ans
    print('-'.join(nums))