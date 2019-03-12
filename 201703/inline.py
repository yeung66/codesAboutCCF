n = int(input())
m = int(input())
lines = [i for i in range(1,n+1)]
for _ in range(m):
    no,move = tuple(map(int,input().split()))
    index = lines.index(no)
    lines.pop(index)
    lines.insert(index+move,no)

print(' '.join(map(str,lines)))