word = input("Give me a word: ")

def is_palindrome(word):
    begin = 0
    end = len(word) - 1
    while begin != end:
        if word[begin] != word[end]:
            return False
        begin += 1
        end -= 1
    return True

result = is_palindrome(word)
print(result)