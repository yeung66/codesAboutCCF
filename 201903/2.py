n = int(input())

for _ in range(n):
    raw = input().replace('/','//').replace('x','*')
    if eval(raw)==24:print('Yes')
    else:print('No')
    
    
