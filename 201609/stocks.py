n = int(input())

stocks = list(map(int,input().split()[:n]))

diff = [abs(stocks[i]-stocks[i-1]) for i in range(1,n)]

print(max(diff))