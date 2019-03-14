n = int(input())
records = input().split(' ')[:n]
result = []
times = {}
for r in records:
    if r in times:
        times[r]+=1
    else:
        times[r]=1
    result.append(times[r])

print(' '.join(map(str,result)))