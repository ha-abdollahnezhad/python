# 1- first app
print("hellow every one")

# 2- python version
import sys
print(sys.version)

# 3- python indentation
if False:
    print("this will work when condition result is true")
else:
    print("this will work when condition result is false")


# 4- python comments
# # -> use for line comment
# """ -> use for multi line comment

# 5- python statements
print("hello i'm hamed.")
"""
if we want write several statements in a single line should use semeicolon (;)
next statement will print content in new line
"""
print("hello ");print("i'm ");print("hamed.")

# 6- print without a new line

print("hello every body", end=" ")
print("i'm learning python.")

# 7- python variables
x = 14
y = "x is : "
print(y,x)
print(type(x))
x = 'sally'
print(y,x)
print(type(x))

X=14 # variable names are case-sensitive
print("x ==> ",x,type(x), "X ==> ", X,type(X))
    # casting
a = str(5)
b = int(5)
c = float(5)

print(a, " ", b, " ", c)

# 8- variable names
"""
legal variable names
    myvar, my_var, _my_var, myVar, MYVAR, myVar2

illegal variable names
    2myvar, my-var, my var

multi words variable namesd
    camel case => myVariableName = "hamed"
    pascal case => MyVariableName = "hamed"
    snake case => my_variable_name = "hamed"

"""

# 9- assign values
x, y, z = "red", "green", "blue"
print(x)
print(y)
print(z)

x = y = z = "pink"
print(x, " ",y," ",z)

    # Unpack a collection
cars = ['tiba', 'pars', 'quick', 'soren', 'dena']

a, b, c, d, e = cars
print(a," ",b," ",c," ",d," ",e)

# 10- global variable
x = 'awesome'
def myFunction():
    global x
    x='fantastic'
    print(x)
myFunction()
print(x)

# 11- data types

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


"""
x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

# 12- numbers 
#int, float, complex
#integer
x = 1
y = 123456789012345678901234567890
z = -1234567890

print(x, " ",y, " ",z)

#float

x = 1.10
y = 1.0
z = -35.59
print(x, " ",y, " ",z)

x = 35e3
y = 12E4
z = -87.7e100

print(x, " ",y, " ", z)

#complex -> Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(x, " ", y, " ",z)

#type conversion
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print (a, " ", b, " ", c)
#Note: You cannot convert complex numbers into another number type.


#random number
import random
print(random.randrange(1, 10))

# 13- strings

print("hello 'ali'", 'hello "mohammad"')

a = """lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt 
ut laborre et dolore magna  aliqua."""
print(a)

a = "Hello, Mohammad!"
print(a[0])

for x in "in god we trust" :
    print(x)

print(len(a))
txt = "in god we trust"
print("free" in txt)
print("god" in txt)

if "we" in txt :
    print("Yes, 'we' is present.")

print("mother" not in txt)
if "light" not in txt :
    print("No, 'light' is not present.") 

# 14- slicing string

a = "hello every body"
print(a[2:11]) #slice from position x to y
print(a[:15]) #slice from start to position y
print(a[6:]) #slice from position x to end
print(a[-16:]) #negative indexing slice sentences from the end
print(a[-8:-1])

# 15- modify strings
a = "in the name of god"
print(a.upper()) #the upper() method returns the string in upper case.
a = "IN THE NAME OF GOD"
print(a.lower()) #the lower() method returns the string in lower case.
a = " in the name of god "
print(a.strip()) #the strip() method removes any whitespace from the beginning or the end.
a = "Hello, World!"
print(a.replace("H", "J")) #the replace() method replace a string with another string.
print(a.split(",")) #the split() method splits the string into substrings if it finds instances of the separator.
print(a.encode())
a = '  hello'
print(a.lstrip())


# 16- String Concatenation
a = "in the name"
b = "of god"
c = a +" "+ b
print(c)

# 17- python - format - strings
# F-Strings

age = 30
txt = f"My name is hamed, I'm {age} years old."
print(txt)

# Placeholders and Modifiers

price = 100
txt = f"The price is {price:.3f} Rials"
print(txt)

txt = f"The price is {22.369 * 45.000569:.7f} Rials"
print(txt)

# 18- Escape Character
# The escape character allows you to use double quotes when you normally would not be allowed.
txt = "my first name is \"Hamed\" but some people call me \"abdollah\" "
print(txt)

#\' single quote
#\\ Backslash
#\n new line
#\r carriage return
#\t tab
#\b backspace
#\f form feed
#\ooo octal value
#\xhh hex value


myTuple = ("mohammad", "ali", "fatemeh")
x = "#".join(myTuple)
print(x)

myDict = {"name": "hamed", "country": "IRAN"}
mySeperator = "test"
x = mySeperator.join(myDict)
print(x)
print(myDict)

# 19- Boolean Values

print(10 > 9)
print(10 < 9)
print(10 == 9)

a = 200
b = 33

if b>a :
    print("b is grater than a")
else :
    print("b is not greater than a")

# Evaluate Values and Variables

print(bool("hello"))
print(bool(15))
print("------------------")
a = "hello"
b = 15
c = 0
d = ""
e = {}
f = []
g = ()
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))

print("-----------------")

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))
print("-----------------")

def myfunction():
    return True

print(myfunction())
print("-----------------")

if myfunction():
    print("!Yes")
else:
    print("!No")
print("-----------------")
x = 200
print(isinstance(x ,int))
print("-----------------")

# 20- Operators
# Arithmetic Operators
x = 15
y = 4
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

"""
python has tow division operators:
/ - Division (return a float)
// - Floor division (return an integer)
"""
# Assignment Operators
"""
x = 5
x += 5 # x = x + 5
x -= 5 # x = x - 5
x *= 5 # x = x * 5
x /= 5 # x = x / 5
x %= 5 # x = x % 5
x //= 5 # x = x // 5
x **= 5 # x = x ** 5

Bitwise Operators
x &= 5 # x = x & 5
x |= 5 # x = x | 5
x ^= 5 # x = x ^ 5
x >>= 5 # x = x >> 5
x <<= 5 # x = x << 5
"""
x = 3
y = 5

x &= y
print(x)

# The Walrus Operator :=

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison Operators
x = 5
y = 3

print(x == y) # equal
print(x != y) # not equal
print(x > y) # greater than
print(x < y) # less than
print(x >= y) # greater than or equal to
print(x <= y) # less than or equal to