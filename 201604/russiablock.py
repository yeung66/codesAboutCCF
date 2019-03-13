m,n = 15,10
board = []

for _ in range(m):
    board.append(list(map(int,input().split()[:n])))
board.append([1 for _ in range(10)])
new = []
for _ in range(4):
    new.append(list(map(int,input().split()[:4])))

pos = int(input())
pos-=1

i = 0
while i <len(new):    
    if sum(new[i])==0:del new[i]
    else:i+=1

new_m = len(new)

new_n = 4

ans = 0
for i in range(15):
    temp = [board[j][pos:pos+new_n] for j in range(i,i+new_m)]
    sumup = [[temp[i][j]+new[i][j] for j in range(new_n)] for i in range(new_m)]
    collsion = False
    for j in range(new_m):
        for k in range(new_n):
            if sumup[j][k]==2:
                collsion=True
                break
        if collsion:break
    if collsion:
        break
    else:ans = i

for i in range(new_m):
    for j in range(new_n):
        if new[i][j]==1:board[ans+i][pos+j]=1

for i in board[:-1]:
    print(' '.join(map(str,i)))
