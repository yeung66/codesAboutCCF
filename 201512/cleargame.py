n,m = tuple(map(int,input().split(' ')))
board = []
for _ in range(n):
    board.append(list(map(int,input().split(' ')[:m])))

row = []

for i in range(n):
    color,count,start = board[i][0],1,0
    for j in range(1,m):
        if board[i][j]==color:count+=1
        else:
            if count>=3:
                row.append((i,start,start+count))
            color,count,start = board[i][j],1,j
    if count>=3:row.append((i,start,start+count))

col = []
for j in range(m):
    color,count,start = board[0][j],1,0
    for i in range(1,n):
        if board[i][j]==color:count+=1
        else:
            if count>=3:
                col.append((j,start,start+count))
            color,count,start = board[i][j],1,i
    if count>=3:col.append((j,start,start+count))

for i,start,end in row:
    for j in range(start,end):board[i][j]=0

for j,start,end in col:
    for i in range(start,end):board[i][j]=0

import time
time.sleep(4)
for row in board:
    print(' '.join(map(str,row)))