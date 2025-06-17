import re 

with open("row.txt", "r") as file:
    from_row = file.read()

output = re.sub(r"[ ,.]", ":", from_row)
print(output)