p = int(input())
privileges = {}
for _ in range(p):
    new = input()
    if ':' not in new:privileges[new]=-1
    else:
        new,high = new.split(':')
        privileges[new]=int(high)

class Role:
    def __init__(self,name):
        self.name = name
        self.privileges = {}

    def appendPrivilede(self,p):
        # print(self.privileges)
        if p.split(':')[0] not in self.privileges:
            self.privileges[p.split(':')[0]]=-1
        # print(self.privileges)
        if ':' in p:
            p,high = p.split(':')
            self.privileges[p]=max(self.privileges[p],int(high))

class User:
    def __init__(self,name):
        self.name=name
        self.privileges={}

roles = {}
r = int(input())
for _ in range(r):
    raw = input().split()
    temp_role = Role(raw[0])
    for p in raw[2:]:temp_role.appendPrivilede(p)
    roles[temp_role.name]=temp_role

u = int(input())
users = {}
for _ in range(u):
    raw = input().split()
    user = User(raw[0])
    users[raw[0]]=user
    for r in raw[2:]:
        role = roles[r]
        for p,no in role.privileges.items():
            if p not in user.privileges:user.privileges[p]=no
            else:
                user.privileges[p]=max(no,user.privileges[p])

tran = {False:'false',True:'true'}

q = int(input())
for _ in range(q):
    name,pri = input().split()
    if name not in users:print(tran[False])
    else:
        user=users[name]
        if ':' in pri:
            pri,no = pri.split(':')
            no = int(no)
            if pri in user.privileges:
                print(tran[user.privileges[pri]>=no])
            else:
                print(tran[False])
        else:
            if pri in user.privileges:
                if user.privileges[pri]==-1:print(tran[True])
                else:
                    print(user.privileges[pri])
            else:
                print(tran[False])