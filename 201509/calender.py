y = int(input())
d = int(input())

month = [31,28,31,30,31,30,31,31,30,31,30,31]

if y%400 == 0 or (y%4==0 and y%100!=0):
    month[1]=29


for i,m in enumerate(month):
    if d<=m:
        ans = (i+1,d)
        break
    else:d=d-m

print(ans[0])
print(ans[1])