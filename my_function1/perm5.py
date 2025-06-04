import itertools

def perm():
    users_string = str(input("Write me something and i will give you permutations of that string!: "))
    perms = itertools.permutations(users_string)
    for i in perms:
        print(" ".join(i))

perm()