m,n = list(map(int,input().split()))

vars = []
trans = {}
raw = []
for _ in range(m):
    row = input()
    i = 0
    while i<len(row)-1:
        if row[i]=='{' and row[i+1]=='{':
            start = i
            while i<len(row)-1 and not (row[i]=='}' and row[i+1]=='}'):i+=1
            i+=2
            vars.append(row[start:i])
        else:
            i+=1
    raw.append(row)
raw = '\n'.join(raw)


for _ in range(n):
    inp = input()
    var= inp.split()[0]
    value = inp[len(var)+2:-1]
    var = '{{ '+var+' }}'
    # print(var,value)
    # raw = raw.replace(var,value)
    trans[var]=value

i = 0
while i<len(raw)-1:
    if raw[i]=='{' and raw[i+1]=='{':
        start=i
        i+=3
        while i<len(raw)-1 and not (raw[i]=='}' and raw[i+1]=='}'):i+=1
        i+=2
        if raw[start:i] in trans:continue
        raw = raw[:start]+raw[i:]
        i = i-start
    else:
        i+=1

for k,v in trans.items():
    # print(k,v)
    raw = raw.replace(k,v)

print(raw)
    