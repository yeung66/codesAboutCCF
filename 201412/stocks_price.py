buy = []
sell = []
records = []
try:
    while True:
        inp = input()
        records.append(inp)
except EOFError:
    pass

i = 0
while i<len(records):
    r = records[i]
    if r and r.startswith('cancel'):
        row = int(r.split()[1])-1
##        if not records[row].startswith('cancel'):
        records[row]=None
        records[i]=None
    i+=1

records = filter(None,records)
for r in records:
    r = r.split()
    price,count = float(r[1]),int(r[2])
    if r[0]=='buy':
        buy.append((price,count))
    else:
        sell.append((price,count))

all_prices = [i[0] for i in sell]
all_prices.extend([i[0] for i in buy])
all_prices = set(all_prices)
ans_price,ans_count = 0,0
for price in all_prices:
    buy_count,sell_count=0,0
    for p,c in buy:
        if p>=price:buy_count+=c
    for p,c in sell:
        if p<=price:sell_count+=c
    count = min(buy_count,sell_count)
    if count>ans_count:ans_price,ans_count=price,count
    elif count==ans_count:ans_price=max(ans_price,price)

print('%.2f'%(ans_price),ans_count)
