T = int(input())
board = []

def judge():
    for row in board:
        if len(set(row))==1 and row[0]!='0':
            return True,row[0]
    for j in range(3):
        # print(board)
        # print(j)
        if board[1][j]!='0' and board[1][j]==board[2][j] and board[2][j]==board[0][j]:
            return True,board[1][j]
    return board[1][1]!='0' and ((board[0][0]==board[1][1] and board[2][2]==board[1][1]) \
                or (board[2][0]==board[1][1] and board[1][1]==board[0][2])),board[1][1]

def points(who):
    count=1
    for i in board:
        for j in i:
            if j=='0':count+=1
    if who=='2':count=-count
    return count

def full():
    for i in board:
        if '0' in i:return False
    return True

def dfs(who):
    if full():return 0
    maxi,mini = -10,10
    for i in range(3):
        for j in range(3):
            if board[i][j]=='0':
                board[i][j]=who
                ok,whoo = judge()
                # print(ok)
                if ok:
                    p = points(who)
                    # print(p)
                    board[i][j]='0'
                    return max(maxi,p) if who=='1' else min(mini,p)
                if who=='1':maxi = max(maxi,dfs('2'))
                else:mini = min(mini,dfs('1'))
                board[i][j]='0'
    # print(maxi,mini)
    return maxi if who=='1' else mini


for _ in range(T):
    board = []
    for _ in range(3):
        board.append(input().split())
    ans,who = judge()
    if ans:
        print(points(who))
    else:
        print(dfs('1'))