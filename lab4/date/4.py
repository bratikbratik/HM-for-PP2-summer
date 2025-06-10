import datetime

x = datetime.datetime.now()
y = datetime.datetime(2025, 2, 10, 15, 30)

def difference(x, y):
    return((x - y).total_seconds())

answ = difference(x, y)
print(answ)