match = input()
flag = False
if input()=='0':
    flag=True
if flag:match=match.lower()
n = int(input())

for _ in range(n):
    test = input()
    if flag and match in test.lower():
        print(test)
    elif match in test:
        print(test) 
    