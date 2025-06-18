import os

A_file = r"/Users/kamillakadyrbaeva/Desktop/PP2/lab6/Z.txt"
B_file = r"/Users/kamillakadyrbaeva/Desktop/PP2/lab6/Y.txt"

with open(A_file, "r") as A, open(B_file, "w") as B:
    for line in A:
        B.write(line)
