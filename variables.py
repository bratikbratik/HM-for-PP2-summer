x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)    # way to output any variable

q = str(3)    # q will be '3', q will be the same as q = "3" and q = '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

w = 5
e = "John"
print(f"Class of variable w = {w}:")
print(type(w))
print()
print(f"Class of variable e = {e}:")
print(type(e))

print()

a = 4
A = "Sally"
print(f"We have variables a = 4 and A = Sally. Proof that A wont overwrite a: {a}, {A}")
#A will not overwrite a

print()

#Legal variable name (contains only a-z and _ and should start with letter)
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar + my_var + MYVAR) # way to output multiple variable

#Multi wird variables:

myVariableName = "John" #camel case
MyVariableName = "John" #pascal case
my_variable_name = "John" #snake case

print()

c = 5
v = 2
print(c + v) # For numbers, the + character works as a mathematical operator

print()

fact = "awesome"

def myfunc():
  print("Python is " + fact)

myfunc()
#Global variables can be used by everyone, both inside of functions and outside

print()

def myfunc2():
    fact = "amazing"
    print("Python is " + fact)

myfunc2()

print()

print("Python is " + fact) # proves the fact that inner variable doesnt work outside its function

print()

def myfunc3():
  global fact2
  fact2 = "fantastic"

myfunc3()

print("Python is " + fact2) #it works cus we created global variable inside of a func3 and
                            #then called it out. also global variable that ws created outside of a
                            #function can be changed inside by using global. ex:
print()

def mufunc4():
    global fact
    fact = "cool"

mufunc4()

print("Python is " + fact)
