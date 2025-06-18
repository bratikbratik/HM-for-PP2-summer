import os

path = r"Users/kamillakadyrbaeva/Desktop/PP2"

if os.path.exists:
    print("The path exists")

filename = os.path.basename(path)
print("Filename of this path:", filename)

dir_portion = os.path.dirname(path)
print("Directory portion of this path:", dir_portion)
