string = input("Give me some words: ").split()

def reverse(string):
    print(" ".join(string) + " -> " + " ".join(string[::-1]))

reverse(string)