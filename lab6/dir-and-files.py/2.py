import os

path = input("Enter the path: ")

if os.path.exists:
    print("Path exists")

if os.access(path, os.R_OK):
    print("You can read the path")

path_writeablity = os.access(path, os.W_OK)
print("Access to write in file:", path_writeablity)

path_executeablity = os.access(path, os.X_OK)
print("Can path be executed:", path_executeablity)