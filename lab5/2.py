import re

with open("row.txt", "r") as file:
    from_row = file.read()

output = re.findall("аб{2,3}", from_row)
print(output)