class IPA:
    def __init__(self,init):
        if '/' in init:
            prefix,self.length = init.split('/')
            ips = list(map(int,prefix.split('.')))
            while len(ips)<4:
                ips.append(0)
            self.ip = tuple(ips)
        else:
            ips = list(map(int,init.split('.')))
            self.length = len(ips)*8
            while ips.__len__()<4:
                ips.append(0)
            self.ip = tuple(ips)
        self.length = int(self.length)
        self.bin = "".join(['%08d'%int(bin(i)[2:]) for i in self.ip])
    def __lt__(self,right):
        return self.ip<right.ip or self.ip==right.ip and self.length<right.length

    def __str__(self):
        return '%d.%d.%d.%d/%d'%(self.ip[0],self.ip[1],self.ip[2],self.ip[3],self.length)

    def inSub(self,ip):
        return self.bin[:self.length]==ip.bin[:self.length]

n = int(input())
ip_list = []
for _ in range(n):
    new = IPA(input())
    ip_list.append(new)

ip_list.sort()

i = 0
while i<len(ip_list)-1:
    if ip_list[i].inSub(ip_list[i+1]):
        ip_list.pop(i+1)
    else:
        i+=1

i = 0
while i<len(ip_list)-1:
    if ip_list[i].length==ip_list[i+1].length:
        new_length = ip_list[i].length-1
        if new_length<0 or ip_list[i].bin[new_length]=='1':
            i+=1
            continue
        ip_list[i].length=new_length
        if ip_list[i].inSub(ip_list[i+1]):
            #ip_list[i] = temp
            ip_list.pop(i+1)
            if i!=0:i-=1
        else:
            ip_list[i].length=new_length+1
            i+=1
        
    else:
        i+=1


for ip in ip_list:
    print(ip)