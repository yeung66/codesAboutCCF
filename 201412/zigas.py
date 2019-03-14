n = int(input())
board = []
for _ in range(n):
    row = input().split()[:n]
    board.append(row)
#print(board)
i,j = 0,0
seq = [board[0][0]]

def right_move():
    global i,j
    j+=1
    seq.append(board[i][j])

def down_move():
    global i
    i+=1
    seq.append(board[i][j])

def left_down():
    global i,j
    while j>0 and i<n-1:
        i,j=i+1,j-1
        seq.append(board[i][j])

def right_up():
    global i,j
    while i>0 and j<n-1:
        i,j=i-1,j+1
        seq.append(board[i][j])

while i!=n-1 or j!=n-1:
    if (i==0 or i==n-1) and j!=n-1:
        right_move()
    else:
        down_move()
    if i==0 or j==n-1:
        left_down()
    else:
        right_up()

print(' '.join(map(str,seq)))
    