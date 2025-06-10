import datetime

x = datetime.datetime.now()
ystrd = int(x.strftime("%d")) - 1
today = x.strftime("%d")
tmrr = int(x.strftime("%d")) + 1

print(f"Today is {today} of February, tommorow is {tmrr} and yesterday was {ystrd}")