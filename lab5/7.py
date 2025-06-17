import re 

# with open("row.txt", "r") as file:
#     from_row = file.read()

from_row = "snake_case_string_becomes_camel_case_string"

output = re.sub(r"_(.)", lambda match: match.group(1).upper(), from_row)
print(output)