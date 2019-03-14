a,b,c,y1,y2 = list(map(int,input().split()))
import datetime

month = str(a) if a>=10 else '0'+str(a)

for year in range(y1,y2+1):
    # '{as}'.format()
    # month = 
    date = datetime.datetime.strptime('%d%s%s'%(year,month,'01'),'%Y%m%d')
    while date.weekday()+1!=c:
        date+=datetime.timedelta(days=1)
    for _ in range(1,b):
        date+=datetime.timedelta(days=7)
    if date.month!=a:print('none')
    else:
        print(date.strftime('%Y/%m/%d'))