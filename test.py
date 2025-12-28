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

# chaining comparison operators
print(1 < x < 10)
print(1 < x and x < y)

# Logical Operators

"""
and -> return true if both statements are true
x < 5 and x < 10
or -> returns true if one of the statements is true
x < 5 or x < 4
not -> reverse the result, returns False if the result is true
not(x < 5 and x < 10)
"""
x = 5
print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

#Identity Operators
"""
is -> returns true if both variables are the same object
is not -> returns true if both variables are not the same object
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not y)

"""
Difference Between is and ==
is - Checks if both variables point to the same object in memory
== - Checks if the values of both variables are equal
"""

# Membership Operators
"""
in -> return true if a sequence with the specified value is present in the object
not in -> returns true if a sequence with the specified value is not present in the object
"""

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("melon" not in fruits)


# Membership in String

text = "hello friends"
print("h" in text)
print("friends" in text)
print("my" not in text)
print("yes" in text)

# Bitwise Operators
"""
& -> AND -> Sets each bit to 1 if both bits are 1
| -> OR -> Sets each bit to 1 if one of two bits is 1
^ -> XOR -> Sets each bit to 1 if only one of two bits is 1
~ -> NOT -> Inverts all the bits
<< -> Zero fill left shift -> Shift left by pushing zeros in from the right and let the leftmost bits fall off
>> -> Signed right shift -> Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""
print(6 & 3)
"""
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the & operator compares the bits and returns 0010, which is 2 in decimal.
"""

print(6 | 3)

"""
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the | operator compares the bits and returns 0111, which is 7 in decimal.
"""

print(6 ^ 3)
"""
The binary representation of 6 is 0110
The binary representation of 3 is 0011

Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.
"""
print(6 << 1)
print(6 >> 1)
print(7 >> 1)
print(10 >> 1)


# Operator Precedence

"""
() -> Parantheses
----------
** -> Exponentiation
----------
+x -x ~x -> Unary plus, unary minus, and bitwise NOT
----------
* / // % -> Multiplication, division, floor division, and modulus
----------
+ - -> Addition and subtraction
----------
<< >> -> Bitwise left and right shifts
----------
& -> Bitwise AND
----------
^ -> Bitwise XOR
----------
| -> Bitwise OR
----------
== != > >=
< <= is    is not  -> Comparisons, identity, and membership operators
in    not in
----------
not -> Logical NOT
----------
and -> AND
----------
or -> OR
----------
"""

print((6 + 3) - (2 + 3))
print(5 + 4 - 7 + 3)

"""
Addition + and subtraction - has the same precedence,
and therefore we evaluate the expression from left to right
"""
# 21-Lists
# List : Lists are used to store
# multiple items in a single variable.

thisList = ['apple', 'banana', 'cherry']
print(thisList)

# Allow Duplicates

thisList = ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(thisList)

# List Length

print(len(thisList))

# List Items - Data Types
list1 = ['apple', 'banana', 'cherry']
list2 = [1, 2, 5, 7, 9, 3]
list3 = [True, False, False]


list4 = ['abcdefg', 34, True, 40, 'male']

print(type(list4))

# The list() Constructor
thisList = list(('apple', 'banana', 'cherry'))
print(thisList)

# Access List Items
print("first item of list : ",thisList[0], "| second item of list : ", thisList[1])

print("Last item by negetive index : ", thisList[-1])

thisList = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thisList[2:5])
"""
Note: The search will start at index 2 (included) and end at index 5 (not included).
"""

print(thisList[:4])
print(thisList[2:])
print(thisList[-4:-1])


if (searchItem := 'watermelon') in thisList:
    print(f"Yes {searchItem} is member of list")
else:
    print(f'{searchItem} is not member of list')

# Change List Item
print("----------\n",thisList)
thisList[1] = 'blackcurrant'
print(thisList)

print("----------")
thisList[1:3] = ['blackcurrant', 'watermelon']
print(thisList)

print("----------")
thisList[1:6] = ['watermelon']
print(thisList)

# Insert Items
print("----------")
thisList.insert(0, "kiwi")
print(thisList)

# Append Items
print("----------")
thisList.append('orange')
print(thisList)

# Extend List
print("----------")
tropical = ['mango', 'pineapple', 'papaya']
thisList.extend(tropical)
print(thisList)

# Add Any Iterable Object
print("----------")
thisList = ['apple', 'banana', 'melon']
thisTuple = ('kiwi', 'cherry')
thisList.extend(thisTuple)
print(thisList)

# Remove List Items
print("----------")
thisList.remove('kiwi')
print(thisList)

print("----------")
thisList.append('banana')
print(thisList)
thisList.remove('banana')
print(thisList)


# Remove Specified Index
print("----------")
thisList.insert(0, 'banana')
print(thisList)
thisList.pop(0)
print(thisList)


print("----------")
print(thisList)
thisList.pop()
print(thisList)

print("----------")
del thisList[1]
print(thisList)
#del thisList # Delete The List Completely.

print("----------")
thisList.clear()
print(thisList)


# Loop Through a List
print("----------")
thisList = ['apple', 'banana', 'cherry']
for x in thisList:
    print(x)
# Loop Through the Index Numbers
print("----------")
for i in range(len(thisList)):
    print(thisList[i])

# Using a While Loop
print("----------")
i = 0
while i < len(thisList):
    print(thisList[i])
    i = i+1

# Looping Using List Comprehension.
# List Comprehension offers the
# shortest syntax for looping through lists
print("----------")
[print(x) for x in thisList]

# List Comprehension
# Based on a list of fruits, you want a new list,
# containing only the fruits with the letter "a" in
# the name.
print("----------")
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList)


print("----------")
newList.clear()
for i in range(len(fruits)):
    if "a" in fruits[i]:
        newList.insert(i,fruits[i])
print(newList)

print("----------")
newList.clear()

newList = [x for x in fruits if "a" in x]
# newList = [expression for item in iterable if condition == True]
print(newList)

print("----------")

newList = [x for x in fruits if x != 'apple']
print(newList)

print("----------")
newList=[x for x in range(10) if x < 5]
print(newList)

print("----------")
newList = [x.upper() for x in fruits]
print(newList)

print("----------")
newList = ['hello' for x in fruits]
print(newList)

print("----------")
newList = [x if x != "banana" else "orange" for x in fruits]
print(newList)

# Sort Lists
# Sort List Alphanumerically
print("----------")
thisList = ['orange', 'mango', 'kiwi', 'pineapple', 'banana', 'apple']
thisList.sort()
print(thisList)

print("----------")
thisList.sort(reverse=True)
print(thisList)

print("----------")
# Customize Sort Function.
# you can also customize your own function by using
# the keyword argument key = function

def myFunc(n):
    return abs(n - 50)

thisList = [100, 50, 65, 82, 23]
thisList.sort(key=myFunc)
print(thisList)

# Case Insensitive Sort
print("----------")
thisList = ['apple', 'Banana', 'Orange', 'kiwi', 'Mango']
thisList.sort()
print(thisList)

print("----------")
thisList.sort(key = str.lower)
print(thisList)

print("----------")
# Reverse Order
thisList.reverse()
print(thisList)