x = "Hello World" # str	
x = 20	          # int	
x = 20.5	  # float	
x = 1j	          # complex	
x = ["apple", "banana", "cherry"]	# list	
x = ("apple", "banana", "cherry")	# tuple	
x = range(6)      # range	
x = {"name" : "John", "age" : 36}	# dict
x = {"apple", "banana", "cherry"}	# set	
x = frozenset({"apple", "banana", "cherry"})	# frozenset	
x = True	  # bool	
x = b"Hello"	  # bytes	
x = bytearray(5)  # bytearray	
x = memoryview(bytes(5))	        # memoryview	
x = None	  # NoneType


#If you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")	
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))	
x = frozenset(("apple", "banana", "cherry"))	
x = bool(5)	
x = bytes(5)
x = bytearray(5)	
x = memoryview(bytes(5))

'''
There are three numeric types in Python:
int
float
complex

Example:
'''

q = 1    # int
y = 2.8  # float
z = 1j   # complex
print(f"Type of number q = {q} is:")
print(type(q))
      
print(f"Type of number y = {y} is:")
print(type(y))
      
print(f"Type of number z = {z} is:")
print(type(z))

print()

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length. Example:
w = 1
a = 35656222554887711
s = -3255522

print(f"w = {w} is:")
print(type(w))
      
print(f"a = {a} is:")
print(type(a))

print(f"s = {s} is:")
print(type(s))

print()

i = 1.10
A = 1.0
M = -35.59
print(f"i = {i} is:")
print(type(i))

print(f"A = {A} is:")
print(type(A))

print(f"M = {M} is:")
print(type(M))

print()

e = 35e3
print(f"e = {e} is:")
print(type(e))
