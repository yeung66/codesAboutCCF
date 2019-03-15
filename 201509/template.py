m,n = list(map(int,input().split()))

trans = {}
raw = []
for _ in range(m):
    row = input()
    raw.append(row)
raw = '\n'.join(raw)


for _ in range(n):
    inp = input()
    var= inp.split()[0]
    value = inp[len(var)+2:-1]
    var = '{{ '+var+' }}'
    trans[var]=value

i = 0
while i<len(raw)-1:
    if raw[i]=='{' and raw[i+1]=='{':
        start=i
        i+=3
        while i<len(raw)-1 and not (raw[i]=='}' and raw[i+1]=='}'):i+=1
        i+=2
        temp = raw[start:i]
        if temp in trans:
            replace = trans[temp]
        else:
            replace = ''
        raw = raw[:start]+replace+raw[i:]
        i = start+len(replace)
    else:
        i+=1

## 直接replace可能会递归解释
##for k,v in trans.items():
##    # print(k,v)
##    raw = raw.replace(k,v)

print(raw)
    
