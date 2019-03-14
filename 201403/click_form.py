class Form:
    def __init__(self,x1,y1,x2,y2,No):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.No = No

    def contain(self,x,y):
        return self.x1<=x<=self.x2 and self.y1<=y<=self.y2

    
n,m = list(map(int,input().split(' ')[:2]))
forms = []
for i in range(n):
    x1,y1,x2,y2 = list(map(int,input().split(' ')[:4]))
    forms.append(Form(x1,y1,x2,y2,i+1))

for _ in range(m):
    x,y = list(map(int,input().split(' ')[:2]))
    hit = False
    for i in range(n-1,-1,-1):
        if forms[i].contain(x,y):
            print(forms[i].No)
            top = forms.pop(i)
            forms.append(top)
            hit = True
            break
    if not hit:print('IGNORED')