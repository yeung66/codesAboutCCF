n,s,t = tuple(map(int,input().split()))
import datetime 
start = datetime.datetime.strptime(str(s),"%Y%m%d%H%M")
end = datetime.datetime.strptime(str(t),"%Y%m%d%H%M")
class time:
    def __init__(self,minute,hour,day,month,weekday):
        self.minute = set(minute)
        self.hour = set(hour)
        self.day = set(day)
        self.month = set(month)
        self.weekday = set(weekday)

months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
weekdays = {'sun':0,'mon':1,'tue':2,'web':3,'thu':4,'fri':5,'sat':6}
days_in_month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

tasks=[]

is_leap = lambda x:x%400==0 or (x%4==0 and x%100!=0)

def process_input(input,t):
    #in input=='*':return list(range())
    minute = input.split(',')

##    if ',' in minute[0]:
##        minute=minute[0].split(',')
    for i,m in enumerate(minute):
        if type(m)==int:continue
        m = m.lower()
        if '-' in m:
            minute.pop(i)
            start,end = m.split('-')
            if str.isalpha(start):start = months[start] if t==0 else weekdays[start]
            if str.isalpha(end):end = months[end] if t==0 else weekdays[end]
            start,end = int(start),int(end)
            minute.extend(list(range(start,end+1)))
        else:
            if str.isalpha(m):m= months[m] if t==0 else weekdays[m]
            minute[i]=int(m)

    return minute

ans = {}

for _ in range(n):
    task = input().split()
    cmd = task[-1]
    minute,hour,day,month,weekday = task[0:-1]
    if minute=='*':minute=list(range(0,60))
    else:minute=process_input(minute,0)
    if hour=='*':hour=list(range(0,24))
    else:hour=process_input(hour,0)
    if day=='*':day=list(range(1,32))
    else:day=process_input(day,0)
    if month=='*':month=list(range(1,13))
    else:month=process_input(month,0)
    if weekday=='*':weekday=list(range(7))
    else:weekday=process_input(weekday,1)

    temp = datetime.datetime.strptime(str(s),"%Y%m%d%H%M")
    while temp.year<=end.year:
        if is_leap(temp.year):days_in_month[2]=29
        else:days_in_month[2]=28
        for m in month:
            for d in day:
                dstr = str(d) if d>=10 else '0'+str(d)
                mostr = str(m) if m>=10 else '0'+str(m)
                if d>days_in_month[m] or (datetime.datetime.strptime(str(temp.year)+mostr+dstr,'%Y%m%d').weekday()+1)%7 not in weekday:continue
                
                for h in hour:
                    hstr = str(h) if h>=10 else '0'+str(h)
                    for ms in minute:
                        mstr = str(ms) if ms >=10 else '0'+str(ms)
                        time = str(temp.year)+mostr+dstr+hstr+mstr
                        if str(s)<=time<str(t):
                            if time in ans:
                                ans[time].append(cmd)
                            else:
                                ans[time]=[cmd]
                
        
        add = 366 if is_leap(temp.year) else 365
        temp+=datetime.timedelta(days=add)

    
ans = [(k,v) for k,v in ans.items()]
ans.sort(key=lambda x:x[0])

for k,v in ans:
    for cmd in v:
        print(k,cmd)
