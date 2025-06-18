import os

path = r"/Users/kamillakadyrbaeva/Desktop/PP2/lab6/W.txt"
filename = os.path.basename(path)

if os.path.exists:
    print("The path exists")

if os.access(path, os.W_OK):
    print("You have permission for deleting. Processing to delete this file...")

os.remove(path)

print("To check if this file deleted, we will check for its existence again")

try:
    if not os.path.exists(path):
        print("The path doesn't exist")
except FileExistsError:
    print("The path has been deleted")

# with open(filename, "w") as file:
#     file.write(f"This is file {filename}")