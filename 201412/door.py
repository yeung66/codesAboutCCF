n = int(input())
records = input().split(' ')[:n]
result = []
times = {str(i):0 for i in range(1,n+1)}
for r in records:
    times[r]+=1
    result.append(times[r])

print(' '.join(map(str,result)))
