raw=[]
try:
    while True:
        raw.append(input())
except EOFError:
    pass
# print(raw)
index = 0
n = len(raw)
process = []
while index<n:
    line = raw[index]
    if not line:
        # print(line,type(line),len(line))
        index+=1
    elif line.startswith('#'):
        level = line.count('#')
        ans = '<h'+str(level)+'>'+line[level:].strip()+'</h'+str(level)+'>'
        process.append(ans)
        # print(ans)
        index+=1
    elif line.startswith('*'):
        ans = '<ul>\n'
        ans+='<li>'+line[1:].strip()+'</li>\n'
        index+=1
        while index<n and raw[index].startswith('*'):
            line = raw[index]
            ans+='<li>'+line[1:].strip()+'</li>\n'
            index+=1
        ans+='</ul>'
        # print(ans)
        process.append(ans)
    else:
        paragraph = []
        paragraph.append(line)
        index+=1
        while index<n and raw[index]:
            # print(raw[index])
            paragraph.append(raw[index])
            index+=1
        paragraph[0]='<p>'+paragraph[0]
        paragraph[-1]=paragraph[-1]+'</p>'
        # print(paragraph)
        process.extend(paragraph)

for line_no,line in enumerate(process):
    i = 0
    while i<len(line):
        if line[i]=='_':
            j = i+1
            while line[j]!='_':
                # print(line[j])
                j+=1
            # print()
            process[line_no]= line = line[:i]+'<em>'+line[i+1:j]+'</em>'+line[j+1:]
            i = i+4
        elif line[i]=='[':
            j=i+1
            while line[j]!=']':j+=1
            text = line[i+1:j]
            jpi = j+2
            while line[jpi]!=')':jpi+=1
            link = line[j+2:jpi]
            process[line_no]=line=line[:i]+'<a href="'+link+'">'+text+'</a>'+line[jpi+1:]
            i+=7+len(link)+1
        else:
            i+=1
            
for i in process:
    print(i)
