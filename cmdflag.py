opts = input()
flags = {}
for i,c in enumerate(opts):
    if c==':' and i!=0:flags['-'+opts[i-1]]=1
    else:flags['-'+opts[i]]=0

n = int(input())
for i in range(n):
    cmd = input().split(' ')[1:]
    #print(cmd)
    ans = {}
    arg = False
    for index,flag in enumerate(cmd):
        # #print(flag)
        # if index>0 and cmd[index-1] in flags and flags[cmd[index-1]]==1:
        #     ans[cmd[index-1]]=flag
        # elif flag in flags:
        #     if flags[flag]==1 and i==len(cmd)-1:break
        #     ans[flag]=False
        # else:break
        if arg:
            ans[cmd[index-1]]=flag
            arg = False
        elif flag in flags:
            if flags[flag]==1:
                arg = True
                if index==len(cmd)-1:break
            else:
                ans[flag] = False
        else:break
    ans = [(k,v) for k,v in ans.items()]
    ans.sort()
    output = "Case %d:"%(i+1)
    for a in ans:
        output+=" "+a[0]
        if a[1]!=False:output+=" "+a[1]
    print(output)
