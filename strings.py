print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

print()

a = "Hello"
print(a)

print()

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#in the result, the line breaks are inserted at the same position as in the code.

print()

a = "Hello, World!"
print(a[1]) #a as an array of letters

for x in "banana":
  print(x)

print()

a = "Hello, World!"
print(f"Length of a = {a} is:")
print(len(a))

print()

txt = "The best things in life are free!"
print("free" in txt) #gives true or false

txt = "The best things in life are free!"
print("expensive" not in txt)

print()

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


b = "Hello, World!"
print(b[2:5]) #from 2 index to 5 (ne vkluchitelno)

b = "Hello, World!"
print(b[:5]) #before fifth index

b = "Hello, World!"
print(b[2:]) #after second index

b = "Hello, World!"
print(b[-5:-2]) #from end, start counting from -1, returns orl

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # the strip() method removes any whitespace from the beginning or the end

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + " " + b #concatenation, only for str
print(c)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars" #_.2f means 2 nums after dot in a number
print(txt)
#f string can be used in print as i did before or in a variable itslef

txt = f"The price is {20 * 59} dollars"
print(txt) #also calculations can be performed

txt = "Hello\nWorld"
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

