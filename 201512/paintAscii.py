import time
test = time.time()
n,m,q = tuple(map(int,input().split(' ')))
board = [['.' for i in range(n)] for i in range(m)]

# visited = set()
direction = [(1,0),(-1,0),(0,1),(0,-1)]
def fill(i,j,char):
    stack = []
    board[j][i]=char
    stack.append((i,j))
    while len(stack)!=0:
        p = stack.pop(0)
        for d in direction:
            x,y = (p[0]+d[0],p[1]+d[1])
            if 0<=x<n and 0<=y<m and board[y][x]!='-' and board[y][x]!='+' and board[y][x]!='|' and board[y][x]!=char:
                board[y][x]=char
                stack.append((x,y)) 
    # if 0<=i<n and 0<=j<m and (i,j) not in visited and board[j][i] not in ('-','|','+'):
    #     board[j][i] = char
    #     visited.add((i,j))
    #     fill(i+1,j,char)
    #     fill(i-1,j,char)
    #     fill(i,j-1,char)
    #     fill(i,j+1,char)

for _ in range(q):
    opera = input().split(' ')
    # print(opera)
    if opera[0]=='1':
        init_x,init_y,char = opera[1:4]
        init_x,init_y = int(init_x),int(init_y)
        # visited = set()
        fill(init_x,init_y,char)
    else:
        x1,y1,x2,y2 = list(map(int,opera[1:5]))
        if x1==x2:
            y1,y2 = min(y1,y2),max(y1,y2)
            for i in range(y1,y2+1):
                if board[i][x1]=='-':board[i][x1]='+'
                elif board[i][x1]!='+':board[i][x1]='|'
        else:
            x1,x2 = min(x1,x2),max(x1,x2)
            for i in range(x1,x2+1):
                if board[y1][i]=='|':board[y1][i]='+'
                elif board[y1][i]!='+':board[y1][i]='-'

board = board[::-1]
for i in range(m):
    print(''.join(board[i]))

print((time.time()-test)*1000)