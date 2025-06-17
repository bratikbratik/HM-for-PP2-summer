import re

with open("row.txt", "r") as file:
    from_txt = file.read()

output = re.findall("аб*", from_txt)
print(output)