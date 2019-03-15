n = int(input())
nums = list(map(int,input().split()[:n]))

hashmap = {}
for i in nums:
    if i in hashmap:hashmap[i]+=1
    else:hashmap[i]=1

##count = [(k,v) for k,v in hashmap.items()]
# print(count)
# 手写选择排序
##for i in range(len(count)-1):
##    for j in range(i+1,len(count)):
##        if count[i][1]<count[j][1] or (count[i][1]==count[j][1] and count[i][0]>count[j][0]):
##            count[i],count[j]=count[j],count[i]

class Pair():
    def __init__(self,i,freq):
        self.i=i
        self.freq=freq

    def __lt__(self,p):
        return self.freq<p.freq or (self.freq==p.freq and self.i>p.i)
    
count = [Pair(k,v) for k,v in hashmap.items()]
count.sort()
for p in count[::-1]:
    print(p.i,p.freq)
