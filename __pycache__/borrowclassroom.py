N,k = list(map(int,input().split()))
keys = [i for i in range(N+1)]

# i = 1
kcount = 0
timeline = {}
for _ in range(k):
    num,start,last = list(map(int,input().split()[:3]))
    if start in timeline:
        timeline[start].append((1,num))
    else:
        timeline[start]=[(1,num)]
    ret_time = start+last
    if ret_time in timeline:
        timeline[ret_time].append((0,num))
    else:
        timeline[ret_time]=[(0,num)]

timeline = [(k,v) for k,v in timeline.items()]
timeline.sort()

for t,issue in timeline:
    # print(issue)
    for i in issue:
        if i[0]==0:
            keys[keys.index(0,1)]=i[1]
        else:
            if i[1] in keys:
                keys[keys.index(i[1])]=0
        # print(keys[1:])
# print(timeline)
print(' '.join(map(str,keys[1:])))