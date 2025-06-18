def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1] #::-1 reverse

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
