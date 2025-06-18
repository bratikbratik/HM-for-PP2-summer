import os

path = r"/Users/kamillakadyrbaeva/Desktop/PP2/lab5/row.txt"

line_cnt = 0

with open(path, "r") as file:
    for line in file:
        line_cnt += 1

print(line_cnt)