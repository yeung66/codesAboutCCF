n = int(input())

pwd = list(filter(None,input().split('/')))

for _ in range(n):
    raw = input()
    path = raw.split('/')
    base = pwd[:]
    if raw.startswith('/'):
        base=[]
        path = path[1:]
    for p in path:
        if not p or p=='.':continue
        elif p=='..':
            if len(base)>0:
                base.pop()
        else:
            base.append(p)
    
    output ='/'+ '/'.join(base)
    #3if raw.startswith('/'):output='/'+ouput
    print(output)
