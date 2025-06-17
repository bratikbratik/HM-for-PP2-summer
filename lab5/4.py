import re

with open("row.txt", "r") as file:
    from_row = file.read()

output = re.findall(r"(?:[а-я][А-Я])+", from_row)
print(output)