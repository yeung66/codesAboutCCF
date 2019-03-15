n = int(input())

class Summon:
    def __init__(self,attr):
        self.pos=attr[0]
        self.attack=attr[1]
        self.health=attr[2]


class Role:
    def __init__(self):
        self.hp = 30
        self.summons = [None]

    def appendSummon(self,summon):
        self.summons.insert(summon.pos,summon)

    def attack(self,i,j):
        i,j=int(i),int(j)
        attacker = self.summons[i]
        if j==0:
            roles[tran[cur_role_index]].hp-=attacker.attack
        else:
            defender = roles[tran[cur_role_index]].summons[j]
            defender.health-=attacker.attack
            if defender.health<=0:roles[tran[cur_role_index]].summons.pop(j)
            attacker.health-=defender.attack
            if attacker.health<=0:cur_role.summons.pop(i)


roles = {1:Role(),-1:Role()}
tran = {1:-1,-1:1}
cur_role_index = 1
cur_role = roles[1]
winner = 0
for _ in range(n):
    action = input().split()
    if action[0]=='end':
        cur_role_index=tran[cur_role_index]
        cur_role=roles[cur_role_index]
    elif action[0]=='summon':
        new = Summon(list(map(int,action[1:])))
        cur_role.appendSummon(new)
    elif action[0]=='attack':
        cur_role.attack(action[1],action[2])
        if roles[tran[cur_role_index]].hp<=0:
            winner = cur_role_index

print(winner)
print(roles[1].hp)
print(len(roles[1].summons)-1,' '.join(map(lambda x:str(x.health),roles[1].summons[1:])))
# print(winner)
print(roles[-1].hp)
print(len(roles[-1].summons)-1,' '.join(map(lambda x:str(x.health),roles[-1].summons[1:])))
