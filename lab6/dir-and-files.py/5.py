import os

path = r"/Users/kamillakadyrbaeva/Desktop/PP2/lab5/row.txt"

list_for_file = []

with open(path, "r") as file:
    for element in file:
        list_for_file.append(element)

print(list_for_file)