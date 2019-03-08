n = int(input())
dp = [[0 for i in range(6)] for i in range(n+1)]

dp[1][0] = 1
mod = 1000000007
for i in range(2,n+1):
    dp[i][0]=1
    dp[i][1]=(2*dp[i-1][1]+dp[i-1][0])%mod
    dp[i][2]=(dp[i-1][2]+dp[i-1][0])%mod
    dp[i][3]=(2*dp[i-1][3]+dp[i-1][1])%mod
    dp[i][4]=(2*dp[i-1][4]+dp[i-1][1]+dp[i-1][2])%mod
    dp[i][5]=(2*dp[i-1][5]+dp[i-1][3]+dp[i-1][4])%mod

print(dp[n][5])