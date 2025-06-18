import os

path = input("Enter the path: ")

try:
    entries = os.listdir(path)

    directories = []

    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            directories.append(entry)
    
    for entry in entries:
        full_path = os.path.join(path, entry)
        print("Checking:", full_path)

    print("\nDirectories")
    for dir in directories:
        print(dir)
    
    print("\nAll entries(files+directories): ")

    for entry in entries:
        print(entry)
    
except FileNotFoundError:
    print("Path doesn't exist")

except PermissionError:
    print("Permission denied")