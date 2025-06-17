import re 

# with open("row.txt", "r") as file:
#     from_row = file.read()

from_row = "SplitAtUppercaseLetters"

output = re.split(r"(?=[A-Z])", from_row)
print(" ".join(output))