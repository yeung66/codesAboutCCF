N = int(input())

N = N // 10
ans = N
x1,left = divmod(N,5)
ans += 2*x1
if left >=3:ans+=1
print(ans)