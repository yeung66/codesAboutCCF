n,m = tuple(map(int,input().split()))

class Node:
    def __init__(self,t,no):
        self.type=t.lower()
        self.id=None
        self.no=no
        self.child = []
        self.parent=None

    def appendChild(self,node):
        node.parent=self
        self.child.append(node)

    def print(self,sep=''):
        print(sep+self.type)
        for c in self.child:
            c.print(sep+' ')

raw = input().split()
root = Node(raw[0],1)
if len(raw)==2:root.id=raw[1][1:]
last_level = 0
last_node = root
for i in range(2,n+1):
    row = input()
    level = row.count('.')//2
    row = row[level*2:]
    row = row.split()
    node = Node(row[0],i)
    if len(row)==2:node.id=row[1][1:]
    if level>last_level:
        last_node.appendChild(node)
        last_level+=1
        last_node=node
    else:
        for _ in range(last_level-level+1):
            last_level-=1
            last_node=last_node.parent
        last_node.appendChild(node)
        last_level+=1
        last_node=node

def dfs(node,sel):
    ans = []
    if len(sel)==1 or type(sel)==str:
        sel = [sel] if type(sel)==str else sel
        if sel[0].startswith('#'):
            if node.id==sel[0][1:]:
                ans.append(node)
                return ans
##            for c in node.child:
##                ans.extend(dfs(c,sel))
        else:
            if node.type==sel[0].lower():ans.append(node)
            for c in node.child:
                ans.extend(dfs(c,sel))
    else:
        
        temp = dfs(node,sel[0])
        # print(temp)
        for temp_node in temp:
            for c in temp_node.child:
                ans.extend(dfs(c,sel[1:]))
    return list(set(ans))

# root.print()
for _ in range(m):
    sel = input().split()
    ans = dfs(root,sel)
    print(len(ans),' '.join(map(str,sorted(map(lambda x:x.no,ans)))))
