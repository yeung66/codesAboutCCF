n = int(input())
seats = [[0 for _ in range(5)] for _ in range(20)]
op = map(int,input().split()[:n])

for num in op:
    close = False
    ans = []
    for i,row in enumerate(seats):
        for j,full in enumerate(row):
            if full==0 and row.count(0)>=num:
                while num>0:
                    ans.append(5*i+j+1)
                    row[j]=1
                    j+=1
                    num-=1
                close=True
                break
        if close:break
    if not close:
        i,j = 0,0
        # print(seats)
        while num>0:
            # print(i,j)
            if seats[i][j]==0:
                seats[i][j]=1
                ans.append(5*i+j+1)
                num-=1
            j+=1
            if j==5:
                j=0
                i+=1

    print(' '.join(map(str,ans)))