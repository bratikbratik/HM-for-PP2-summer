def permute(s, chosen=""):
    if not s:
        print(chosen)
    else:
        for i in range(len(s)):
            new_chosen = chosen + s[i]
            new_s = s[:i] + s[i+1:]
            permute(new_s, new_chosen)

user_input = input("Enter a string: ")
permute(user_input)
