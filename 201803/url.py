n,m=list(map(int,input().split()))
paths = {}

for _ in range(n):
    path,name = input().split()
    paths[name]=path.split('/')

for _ in range(m):
    query = input().split('/')
    total = False
    for name,path in paths.items():
        match=True
        i,j = 0,0
        args = []
        if len(query)<len(path):continue
        while i<len(path):
            term = path[i]
            if not term.startswith('<'):
                if term==query[i]:i+=1
                else:
                    match=False
                    break
            else:
                if term=='<int>' and str.isnumeric(query[i]):
                    for j in range(len(query[i])):
                        if query[i][j]!='0':
                            query[i]=query[i][j:]
                            break
                    args.append(query[i])
                    i+=1
                elif term=='<str>':
                    args.append(query[i])
                    i+=1
                elif term=='<path>':
                    args.append('/'.join(query[i:]))
                    j = len(query)
                    break
                else:
                    match=False
                    break
            j=i
        if match and j==len(query):
            total=True
            break
    if total:
        print(name,' '.join(args))
    else:
        print(404)
        
        
                    
