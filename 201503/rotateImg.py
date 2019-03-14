n,m = tuple(map(int,input().split(' ')))

matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split()[:m])))

for i in range(m-1,-1,-1):
    row = []
    for j in range(n):
        # print(j,i)
        row.append(matrix[j][i])
    print(' '.join(map(str,row)))