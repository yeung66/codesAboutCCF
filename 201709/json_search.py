import json

n,m = list(map(int,input().split(' ')))
raw = ''
for _ in range(n):
    raw+=input()

ans = json.loads(raw)

for _ in range(m):
    query = input()
    query = query.split('.')
    temp = ans
    flag = False
    for q in query:
        if q in temp:temp = temp[q]
        else:
            print('NOTEXIST')
            flag=True
            break
    if flag:continue
    if type(temp)==str:print('STRING '+temp)
    else:print('OBJECT')