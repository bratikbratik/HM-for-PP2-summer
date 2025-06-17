import datetime

x = datetime.datetime.now()
ystrd = int(x.strftime("%d")) - 1
today = int(x.strftime("%d"))
tmrr = int(x.strftime("%d")) + 1

month = int(x.strftime("%m"))

months = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]

print(f"Today is {today} of {months[month - 1]}, tommorow is {tmrr} and yesterday was {ystrd}")