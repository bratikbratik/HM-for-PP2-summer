import re

with open("row.txt", "r") as file:
    from_row = file.read()

output = re.findall("а.*б", from_row)
print(output)