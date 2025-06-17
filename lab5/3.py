import re

with open("row.txt", "r") as file:
    from_txt = file.read()

output = re.findall(r"[а-ёь]+(?:_[а-ёь]+)+", from_txt)
print(output)