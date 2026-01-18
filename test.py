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

# Copy List
"""
You cannot copy a list simply by typing list2 = list1, because: list2 will
only be a reference to list1, and changes made in list1 will
automatically also be made in list2.
"""

# Use copy() method
print("----------")
myList = thisList.copy()
print(myList)

# Use the list() method
print("----------")
thisList.append('peach')
myList = list(thisList)
print(myList)

# Use the slice operator
print("----------")
myList = thisList[:]
print(myList)

# Join Two Lists
print("----------")
list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]
list3 = list1 + list2
print(list3)

print("----------")
for x in list2:
    list1.append(x)
print(list1)

print("----------")
list1.extend(list2)
print(list1)

# 22-Tuples
# Tuples are Ordered and unchangeable.Allows duplicate members.
print("----------")
myTuple = ('apple', 'banana', 'cherry', 'mango', 'apple', 'melon')
print(myTuple)

print("----------")
print('tuple length is: ', len(myTuple))

print("----------")
myTuple = ('apple',)
print(type(myTuple))

print("----------")
myTuple = ('apple')
print(type(myTuple))

print("----------")
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ('abcd', 35, True, 50, 'male')
print(type(tuple4))

# the tuple() Constructor
print("-------------------")
thisTuple = tuple(('apple', 'banana', 'cherry', 'mango', 'watermelon'))
print(thisTuple)

# Access Tuple Items
print("-------------------")
print(thisTuple[1])

# Negative Indexing
print("-------------------")
print(thisTuple[-1])

# Range of Indexes
print("-------------------")
print(thisTuple)
print(thisTuple[1:4])
print(thisTuple[2:])
print(thisTuple[:3])
print(thisTuple[-6:-1])

if 'apple' in thisTuple:
    print('Yes, "apple" is in the tuple')

print("-------------------")
# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples
# are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list,
# change the list, and convert the list back into a tuple

print(thisTuple)
y = list(thisTuple)
y[1] = 'kiwi'
thisTuple = tuple(y)
print(thisTuple)

print("-------------------")
# Add Items
# Since tuples are immutable, they do not have a built-in append()
# method, but there are other ways to add items to a tuple.
print(thisTuple)
y = list(thisTuple)
y.append('banana')
thisTuple = tuple(y)
print(thisTuple)

print("-------------------")
# Add tuple to a tuple
y = ('grap',)
thisTuple += y
print(thisTuple)

print("-------------------")
# Remove Items
# Note: You cannot remove items in a tuple.

y = list(thisTuple)
y.remove('grap')
thisTuple = tuple(y)
print(thisTuple)

#del thisTuple

print("-------------------")
thisTuple = ('apple', 'banana', 'cherry')
(apple, banana, cherry) = thisTuple
print(apple)
print(banana)
print(cherry)

print("-------------------")
# Note: The number of variables must match the number of values
# in the tuple, if not, you must use an asterisk to collect the
# remaining values as a list.

# Using Asterisk

thisTuple = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
(green, yellow, *red) = thisTuple
print(green)
print(yellow)
print(red)

print("-------------------")
(green, *tropic, red) = thisTuple
print(green)
print(tropic)
print(red)


# Loop Tuples
# Loop Through a Tuple
print("-------------------")
for x in thisTuple:
    print(x)

# Loop Through the Index Numbers
print("-------------------")
for i in range(len(thisTuple)):
    print(thisTuple[i])

# Using a While Loop
print("-------------------")
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i = i+1

# Join Tuples
print("-------------------")
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
print("-------------------")
fruits = ('apple', 'banana', 'cherry')
myTuple = fruits * 2
print(myTuple)

# Tuple Methods
print("-------------------")
print(thisTuple)
print(thisTuple.count('apple'))
print(thisTuple.index('cherry'))


print("-------------------")

# 23- Phyton Sets
"""
A set is a collection which is unordered, unchangeable*, and unindexed.
Set items are unorderd, unchangeable, and do not allow duplicate values.
"""

thisSet = {'apple', 'banana', 'cherry', 'melon', 'kiwi'}
print(thisSet)
print("-------------------")

"""Once a set is created, you cannot change its items, but you can remove
items and add new items.
Set cannot have two items with the same value.
Note : The value True and 1 are considered the same value in sets, and are
treated as duplicates.
Note : The values False and 0 are considered the same value in sets, and are
treated as duplicates
"""


thisSet = {'apple', 'banana', 'cherry', 'pineapple', 'melon', 'apple', 1, True}
print(thisSet)

thisSet = {'apple', 'banana', 0, False}
print(thisSet)
print("-------------------")

print(len(thisSet))
print("-------------------")
set1 = {'vahid', 'majid', 'mobid'}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False, False}
set4 = {'hakim', 35, True, 999, 'male'}

print(type(set4))
print("-------------------")
# The set() Constructor
thisSet = set(('apple', 'banana', 'cherry'))
print(thisSet)

print("-------------------")
# Access Set Items
"""
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a
specified calue is present in a set, by using the in keyword.
Once a set is created, you cannot change its items, but you can add new
Items.
"""
for x in thisSet:
    print(x)
print("-------------------")

print('banana' in thisSet)
print('banana' not in thisSet)
print("-------------------")

# Add Set Items

thisSet.add('blubery')
print(thisSet)
print("-------------------")

mySet = {'orange', 'pineapple', 'mango'}
thisSet.update(mySet)
print(thisSet)
print("-------------------")

mySet = ['kiwi', 'melon', 'apple']
thisSet.update(mySet)
print(thisSet)
print("-------------------")

# Remove Set Items

thisSet.remove('mango')
print(thisSet)
print("-------------------")
# Note: If the item to remove does not exist, remove(). will raise an error.

thisSet.discard('blubery')
print(thisSet)
print("-------------------")

# Note: If item to remove does not exist, discard(). will NOT raise an error.

# Loop Sets
i = 1
for x in thisSet:
    print(f"{i} : {x}")
    i = i+1
del i
print("-------------------")

# Join Sets
"""
There are several ways to join two or more sets in Python.
The union() an update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are
not in the other set(s).
The symmetric_difference() method keeps all items except the duplicates.
"""

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
# set3 = set1.union(set2)

# You can use the | operator instead of the union() method, and you will
# get the same result.
set3 = set1 | set2
print(set3)
print("-------------------")

# Join Multiple Sets

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = {'john', 'elena'}
set4 = {'apple', 'banana', 'cherry'}

mySet = set1.union(set2, set3, set4)
print(mySet)
print("-------------------")


mySet = set1 | set2 | set3 | set4
print(mySet)
print("-------------------")

# Join a Set and a Tuple
thisSet = {'a', 'b', 'c'}
thisTuple = (1, 2, 3)
thisTS = thisSet.union(thisTuple)
print(thisTS)
print("-------------------")

# Update
# Note: Both union() and update() will exclude any duplicate items.
set1.update(set2)
print(set1)
print("-------------------")

# Intersection
# Keep ONLY the duplicates

set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}

set3 = set1.intersection(set2)
print(set3)
print("-------------------")

print(set1 & set2)
print("-------------------")

# Note: The & operator only allows you to join sets with sets,
# and not with other data types like you can with intersection() method.

set1.intersection_update(set2)
print(set1)
print("-------------------")

set1 = {'apple', 1, 'banana', 0, 'cherry'}
set2 = {False, 'google', 1, 'apple', 2, True}

set3 = set1.intersection(set2)
print(set3)
print("-------------------")


# Difference

print(set1.difference(set2))
print("-------------------")

# You can use the - operator instead of the difference() method
# and you will get the same result.

set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}

set3 = set1 - set2
print(set3)
print("-------------------")

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that
# are NOT in both sets.

set3 = set1.symmetric_difference(set2)
print(set3)
print("-------------------")

set3 = set1 ^ set2
print(set3)
print("-------------------")

# The symmetric_difference_update() method will also keep all but the
# duplicates, but it will change the original set instead of returning a
# a new set.

set1.symmetric_difference_update(set2)
print(set1)
print("-------------------")


# Python frozenset
"""
frozenset is an immutable version of a set.
like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset.
"""

x = frozenset({'apple', 'banana', 'cherry'})
print(x)
print(type(x))
print("-------------------")

y = frozenset({1, 2, 3, 4})
print(x | y)
print("-------------------")

# 24- Python Dictionaries
"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not
allow duplicates.
"""
thisDict = {
    'brand' : 'ford',
    'model' : 'Mustang',
    'year' : 1964
}

print(thisDict)
print("-------------------")

# Dictionary Items
print(thisDict["brand"])
print("-------------------")

thisDict = {
    'brand' : 'ford',
    'model' : 'mustang',
    'year' : 1964,
    'year' : 2020
}

print(thisDict)
print("-------------------")

print(len(thisDict))
print("-------------------")

thisDict = {
    'brand' : 'ford',
    'electric' : False,
    'year' : 1964,
    'colors': ['red', 'white', 'blue']
}

print(thisDict)
print(type(thisDict))
print("-------------------")

thisDict = dict(name = 'john', age = 30, country = 'US')
print(thisDict)
print("-------------------")

# Access Dictionary Items

x = thisDict['name']
print(x)
print("-------------------")

x = thisDict.get('country')
print(x)
print("-------------------")

# Get Keys

x = thisDict.keys()
print(x)
print("-------------------")

car = {
    'brand' : 'ford',
    'model' : 'Mustang',
    'year' : 1964
}
x = car.keys()
print(x)
car['color'] = ['black', 'red', 'white']
print(x)
print("-------------------")

# Get Values

x = car.values()
print(x)
car['year'] = 2020
print(x)
print("-------------------")


# Get Items

x = car.items()
print(x)
car['speed'] = 220
print(x)
print("-------------------")

# Check if key Exists

if 'model' in car :
    print('Yes, \'model\' is one of the keys in the car dictionary')

# Change Dictionary Items

print(thisDict)
thisDict['name'] = 'ali'
print(thisDict)
print("-------------------")

thisDict.update({'country': 'iran'})
print(thisDict)
print("-------------------")

# Adding Items

thisDict['birth-date'] = '1380-01-10'
print(thisDict)
print("-------------------")

thisDict.update({'born-city' : 'tehran'})
print(thisDict)
print("-------------------")

# Remove Dictionary Items

thisDict.pop('birth-date')
print(thisDict)
print("-------------------")

thisDict.popitem()
print(thisDict)
print("-------------------")

del thisDict['age']
print(thisDict)
print("-------------------")


# del thisDict # The del keyword can also delete the dictionary completely.

myDict.clear()
print(myDict)
print("-------------------")

# Loop Dictionaries

for x in thisDict.values():
    print(x)
for x in thisDict.keys():
    print(x)
print("-------------------")

for x,y in thisDict.items():
    print(f'{x} : {y}')
print("-------------------")

# Copy Dictionaries
myDict = thisDict.copy()
print(myDict)
print("-------------------")

myDict = dict(thisDict)
print(myDict)
print("-------------------")

# Nested Dictionaries
myCars = {
    'BMW' : {
        'color' : 'light-blue',
        'model' : 'i8',
        'year' : 2022
    },
    'ferari' : {
        'color' : 'light-orange',
        'model' : '580',
        'year' : 2023
    },
    'ford' : {
        'color' : 'white',
        'model' : 'mustang',
        'year' :2025
    }
}
print(myCars)
print("-------------------")

print(myCars['ford']['model'])
print("-------------------")

# Loop Through Nested Dictionaries
for x, obj in myCars.items() :
    print(x)
    for y in obj :
        print(y + ' : ', obj[y])
print("-------------------")

# 25- Python If Statement
a = 33
b = 33
if a > b :
    print("a is greater than b")
elif a == b :
    print('a and b are equal')
print("-------------------")

score = 55
if score >= 90 :
    print('Grade: A')
elif score >= 80 :
    print('Grade: B')
elif score >= 70 :
    print('Grade: C')
elif score >= 60 :
    print('Grade: D')
else :
    print('Grade: E')
print("-------------------")

# Short Hand If

a = 5
b = 4
if a > b : print('a is greater than b')
print("-------------------")

# Short Hand If ... Else

a = 2
b = 313
print('a') if a > b else print('b')
print("-------------------")

bigger = a if a > b else b
print('bigger is : ', bigger)
print("-------------------")

a = 313
b = 310
print('A') if a > b else print('=') if a == b  else print('B')
print("-------------------")

# Python Logical Operators
a = 200
b = 33
c = 300

if a > b and c > a :
    print('Both conditions are True')
if a > b or a > c :
    print('At least one of the conditions is True')
if not a > b :
    print('a is NOT greater than b')
print("-------------------")

age = 25
is_student = False
has_discount_code = True

if(age < 18 or age > 65) and not is_student or has_discount_code:
    print("discount applies!")
print("-------------------")

temperature = 25
is_raining = False
is_weekend = True

if(temperature > 20 and not is_raining) or is_weekend:
    print('Great day for outdoor activities!')

print("-------------------")
username = 'Hamed'
password = 'secret123'
is_verified = True

if username and password and is_verified :
    print('Login successful')
else :
    print('Login Failed')
print("-------------------")

score = 85
attendance = 90
submitted = True

if score >= 60 :
    if attendance >= 80 :
        if submitted :
            print('Pass with good standing')
        else :
            print('Pass but missing assignment')
    else :
        print('Pass but low attendance')
else :
    print('Fail!')
print("-------------------")

# Python Pass Statement
value = 50
if value < 0 :
    print('Negative value')
elif value == 0 :
    pass
else :
    print('Positive value')
print("-------------------")

# 26- Python Match

# The Python Match Statement

day = 7
match day :
    case 1:
        print('Monday')
    case 2:
        print('Tuseday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Not Week Day')
print("-------------------")

day = 4
match day :
    case 1 | 2 | 3 | 4 | 5:
        print('Today is a weekday')
    case 6 | 7:
        print('I Love weekends!')
print("-------------------")

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if month == 4:
        print('A weekday in April')
    case 1 | 2 | 3 | 4 | 5 | 6 | 7 if month == 5:
        print('A weekday in May')
    case _:
        print('NOT a weekday')
print("-------------------")

# 27- Python Loops
# The while Loop

i = 1
while i < 6 :
    print(i)
    i += 1
print("-------------------")

# The break Statement
i = 1
while i < 6 :
    print(i)
    if i == 3 :
        break
    i += 1
print("-------------------")

# The continue Statement
i = 0
while i < 6 :
    i += 1
    if i == 3 :
        continue
    print(i)
print("-------------------")

# The else Statement
i = 8
while i < 6 :
    print(i)
    i += 1
else :
    print('i is no longer less than 6')
print("-------------------")

# Note: The else block will NOT be executed
# if the loop is stopped by a break statement.

# 28- Python For Loops
fruits = ['apple', 'banana', 'cherry', 'mango', 'melon']
for x in fruits :
    print(x)
print("-------------------")

for x in 'banana':
    print(x)
print("-------------------")

for x in fruits:
    if x == 'banana':
        break
    print(x)
print("-------------------")

for x in fruits:
    if x == 'cherry':
        continue
    print(x)
print("-------------------")

for x in range(6):
    print(x)
print("-------------------")

for x in range(2, 6):
    print(x)
print("-------------------")

for x in range(2, 30, 3):
    print(x)
print("-------------------")

for x in range(6):
    print(x)
else:
    print('finally finished')
print("-------------------")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print('finally finished!')
print("-------------------")

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)
print("-------------------")

for x in [0, 1, 2]:
    pass
print("-------------------")

# 29- Python Functions
def my_function():
    print('hello every body')

my_function()
print("-------------------")

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print("-------------------")

def my_function():
    pass

my_function()
print("-------------------")

# Python Function Arguments
def my_function(name): # name is a parameter
    print('Hello, Welcome', name)
my_function('hamed') # hamed is an argument
print("-------------------")

# Number of Arguments
def my_function(fname, lname) :
    print(fname + " " + lname)
my_function('hamed', 'abdollahnezhad')
print("-------------------")

# my_function('vahid') # you will get an error

# Default Parameter Values
def my_function(name = 'friend'):
    print('hello', name)
my_function('hamed')
my_function()
print("-------------------")

# Keyword Arguments
# the order of the arguments does not matter.
print("-------------------")
def my_function(car, model):
    print('i have a ', car)
    print('my ',car ,' model is ',model)

my_function(car='pride', model='151')

# Positional Arguments
# The order matters with positional arguments
def my_function(car, model):
    print('i have a', car)
    print('my ', car, 'model is', model)
my_function('pride', '151')
print("-------------------")

# Mixing Positional and Keyword Arguments
# However, positional arguments must come before keyword arguments
def my_function(car, model, production_date):
    print('i have a', car, 'model is ', model, ', production date is ', production_date)
my_function('pride', model='151', production_date='1401-8-30')
print("-------------------")

# Passing Different Data Types
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ['apple', 'banana', 'cherry', 'mango']
my_function(my_fruits)
print("-------------------")

def my_function(person):
    print('Name is : ', person['name'])
    print('Age is : ', person['age'])
my_person = {'name':'ali', 'age':'25'}
my_function(my_person)
print("-------------------")

# Return Values
def my_function(x, y):
    return x + y
result = my_function(5, 3)
print(result)
print("-------------------")

# Returning Different Data Types

def my_function():
    return ['apple', 'banana', 'cherry']
fruits = my_function()
print(fruits[0], fruits[1], fruits[2])
print("-------------------")

def my_function():
    return (10, 20)
x, y = my_function()
print('x :', x)
print('y :', y)
print("-------------------")

# Positional-Only Arguments
# To specify positional-only arguments, add , / after the arguments
def my_function(name, /):
    print('Hello,', name)
my_function('Hamed')
print("-------------------")

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments
# , add *, before the arguments

def my_function(*, name):
    print('Hello,', name)
my_function(name = 'Hamed')
print("-------------------")

# Combining Positional-Only and Keyword-Only
# Arguments before / are positional-only, and
# arguments after * are keyword-only

def my_function(a, b, /, *, c, d):
    return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)
print("-------------------")

# Python *args and **kwargs
# If you do not know how many arguments will be passed into your
# function, add a * before the parameter name.
def my_function(*kids):
    print('kids name\'s are : ')
    for kid in kids:
        print(kid)

my_function('emil', 'tobias', 'linus')
print("-------------------")

# Using *args with Regular Arguments
# Regular parameters must come before *args

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
my_function('Hello', 'ali', 'hojat', 'hadi', 'karim')
print("-------------------")

def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
print("-------------------")

def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num :
            max_num = num
    return max_num

print(my_function(1, 2, 3, 8, 35, 10, 15, 20))
print("-------------------")

# Arbitrary Keyword Arguments - **kwargs

def my_function(**kids):
    print('First name: ' + kids['fname'] + ' | Last name: ' + kids['lname'] + ' | age :' , kids['age'])

my_function(fname = 'ali', lname = 'hoseini', age = 18)
print("-------------------")


# **kwargs with Regular Arguments

def my_function(username, **details):
    print('Username :', username)
    print('Aditional details:')
    for key , value in details.items():
        print(' ', key + ':', value)
my_function('hamed123', age = 30, city = 'tehran', hobby = 'coding')
print("-------------------")

# Combining *args and **kwargs
# The order must be :
# 1.regular parameter - 2.*args - 3.**kwargs
def my_function(title, *args, **kwargs):
    print('titel :', title)
    print('positional arguments :', args)
    print('keyword arguments :', kwargs)

my_function('User Info', 'Email : hamed@email.com', 'city : Tehran', 40, age = 30, work_title = 'programmer', work_start = '1390-02-01')
print("-------------------")


# Unpacking Arguments
# Unpacking Lists with *

def my_function(a, b, c):
    return a + b + c
numbers = [1, 2 ,3]
result = my_function(*numbers)
print('the result is :',result)
print("-------------------")

# Unpacking Dictionaries with **
def my_function(fname, lname, age):
    print('Hello', fname, lname, age, ' year\'s old')
person = {'fname' : 'hamed', 'lname' : 'alavi', 'age' : '30'}
my_function(**person)
print("-------------------")

# Python Scope
# A variable is only available from inside the
# region it is created. This is called scope.

# Local Scope
x = 999
def my_func():
    x = 300
    print(x)
my_func()
print(x)
print("-------------------")

def myFunc():
    x = 100
    def myInnerFunc():
        print(x)
    myInnerFunc()
myFunc()
print("-------------------")

x = 500
def myFunc():
    print(x)

myFunc()
print(x)
print("-------------------")

# Global Keyword
# If you need to create a global variable, but are stuck in
# the local scope, you can use the global keyword.
# the global keyword makes the variable global.

def myFunc():
    global x 
    x = 777
myFunc()
print(x)
print("-------------------")

# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside 
# nested functions.
# The nonlocal keyword makes the variable belong to the
# outer function. 

def myFunc1():
    x = 'hamed'
    def myFunc2():
        nonlocal x 
        x = 'hello'
    myFunc2()
    return x 
print(myFunc1())
print("-------------------")

# The LEGB Rule
'''
Python follows the LEGB rule when looking up variable names,
and searches for them in this order:
1. Local - Inside the current function
2. Enclosing - Inside enclosing functions (from inner to outer)
3. Global - At the top level of the module
4. Built-in - In Pytho's built-in namespace
'''
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print('Inner:', x)
    inner()
    print('Outer:', x)
outer()
print('Global:', x)
print("-------------------")

# Python Decorators
'''
Decorators let you add extra behavior to a function,
without changing the function's code.
A decorator is a function that takes another function
as input and returns a new function.
'''
# Basic Decorator
# Define the decorator first, then apply it with @decorator_name
# above the function.

def changecase(func):
    def myInner():
        return func().upper()
    return myInner

@changecase
def myFunction():
    return 'Hello Hamed'
print(myFunction())
print("-------------------")

'''
By placing @changecase directly above the function definition,
the function myfunction is being "decorated" with the 
changecase function.
The function changecase is the decorator.
The function myfunction is the function that gets decorated.
'''

# Multiple Decorator Calls
# A decorator can be called multiple times. Just place the
# decorator above the function you want to decorate.

def changecase(func):
    def myInner():
        return func().upper()
    return myInner

@changecase
def myFunction():
    return 'Hello Hamed'

@changecase
def otherFunction():
    return 'I am speed!'
print(myFunction())
print(otherFunction())

# Multiple Decorators
'''
You can use multiple decorators on one function.
This is done by placing the decorator calls on top of each other.
Decorators are called in the reverse order, starting with the
one closest to the
'''
def changecase(func):
    def myInner():
        return func().upper()
    return myInner

def addGreeting(func):
    def myInner():
        return 'Hello ' + func() + ' Have a good day!'
    return myInner

@changecase
@addGreeting
def myFunction():
    return 'Hamed'
print(myFunction())
print("-------------------")

# Preserving Function Metadata
# Functions in Python has metadata that can be accessed
# using the __name__ and __doc__ attributes.
# But, when a function is decorated, the metadata of the original
# function is lost.
# To fix this, Python has a built-in function called
# functools.wraps that can be used to preserve the original
# function's name and docstring.

def myFunction():
    return 'Have a greate day!'
print(myFunction.__name__)
print("-------------------")

def changecase(func):
    def myInner():
        return func().upper()
    return myInner

@changecase
def myFunction():
    return 'Have a greate day!'

print(myFunction.__name__)
print(myFunction())
print("-------------------")

import functools

def changecase(func):
    @functools.wraps(func)
    def myInner():
        return func().upper()
    return myInner

@changecase
def myFunction():
    return 'Have a greate day !'

print(myFunction.__name__)
print("-------------------")

# Python Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but
# can only have one expression.

x = lambda a : a + 10
print(x(5))
print("-------------------")

x = lambda a, b : a * b
print(x(10, 10))
print("-------------------")

x = lambda a, b, c : a + b + c
print(x(1, 2, 3))
print("-------------------")

def myFunction(n):
    return lambda a : a * n

myDoubler = myFunction(2)
print(myDoubler(20))
print("-------------------")

myTripler = myFunction(3)
print(myTripler(10))
print("-------------------")

# Lambda with Built-in Function
# Using Lambda with map()

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)
print("-------------------")

# Using Lamba with filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
print(odd_numbers)
print("-------------------")

# Using Lambda with sorted()

students = [('emil', 25), ('tobias', 22), ('linus', 28)]
sorted_students = sorted(students, key = lambda x : x[1])
print(sorted_students)
print("-------------------")

words = ['apple', 'pie', 'banana', 'cherry']
sorted_words = sorted(words, key = lambda x : len(x))
print(sorted_words)

# Python Recursion
# Recursion is when a function calls itself.

def countdown(n):
    if n <= 0 :
        print('done!')
    else:
        print(n)
        countdown(n - 1)

countdown(10)
print("-------------------")

# Base Case and Recursive Case
# Every recursive function must have two parts:
'''
A base case - A condition that stop the recursion
A recursive case - The function calling itself with a modified argument

Without a base case, the function would call itself forever,
causing a stack overflow error.
'''
def factorial(n):
    # Base case
    if n == 0 or n == 1 :
        return 1
    # Recursive case
    else :
        return n * factorial(n - 1)
    
print(factorial(5))
print("-------------------")

# The base case is crucial. Always make sure your recursive function
# has a condition that will eventually be met.

def fibonacci(n):
    if n <= 1 :
        return n
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(14))
print("-------------------")

# Recursion with Lists

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        print(f'numbers[0] : {numbers[0]} , numbers[1:] : {numbers[1:]}')
        return numbers[0] + sum_list(numbers[1:])
    
myList = [3, 4, 5, 6, 7, 8, 9]
print(sum_list(myList))
print("-------------------")

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        print(f'numbers[0] : {numbers[0]} , numbers[1:] : {numbers[1:]} , max : {max_of_rest}')
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
myList = [3, 7, 2, 9, 1]
print(find_max(myList))
print("-------------------")

def walk(steps):
    if steps <= 0:
        return
    else:
        walk(steps - 1)
        print(f'You take step #{steps}')

walk(100)
print("-------------------")

# Recursion Depth Limit
# Python has a limit on how deep recursion can go. The default
# limit is usually around 1000 recursive calls.

import sys
print(sys.getrecursionlimit())
print("-------------------")

# If you need deeper recursion, you can increase the limit, but
# be careful as this can cause crashes:

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
print("-------------------")

# Note: Increasing the recursion limit should be done with caution.
# For very deep recursion, consider using iteration instead.

# Python Generators
'''
Generator are functions that can pause and resume their execution.
When a generator function is called, it returns a generator object,
which is an iterator.
The code inside the function is not executed yet, it is only compiled.
The function only executes when you iterate over the generator.
'''

def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)
print("-------------------")

'''
Generators allow you to iterate over data without storing the
entire dataset in memory.
Instead of using return, generators use the yield keyword.
'''
# The yield keyword
'''
The yield keyword is what makes a function a generator.
When yield is encountered, the function's state is saved,
and the value is returned. The next time the generator is called,
it continues from where it left off.
'''

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
print("-------------------")

'''
Unlike return, which terminates the function, yield pauses it
and can be called multiple times.
'''

# Generators Saves Memory
'''
Generators are memory-efficient because they generate values 
on-the-fly instead of storing everything in memory.

For large datasets, generators save memory:
'''

def large_sequence(n):
    for i in range(n):
        yield i
# This does't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("-------------------")

# Using next() with Generators
'''
You can manually iterate through a generator using the next()
function:
'''
def simple_gen():
    yield 'hamed'
    yield 'ali'
    yield 'majid'
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print("-------------------")

# When there are no more values to yield, the generator raises
# a StopIteration exception:

def simple_gen():
    yield 1
    yield 2
gen = simple_gen()
print(next(gen))
print(next(gen))
#print(next(gen))
print("-------------------")

# Generator Expressions
'''
Similar to list comprehensions, you can create generators using
generator expressions with parentheses instead of square brackets:
'''
# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))
print("-------------------")

# Example
# Using a generator expression with sum:

# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)
print("-------------------")

# Fibonacci Sequence Generator

'''
Generators can be used to create the fibonacci sequence.
It can continue generating values indefinitely, whithout running
out of memory:
'''

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# Get first 100 fibonacci numbers
gen = fibonacci()
for _ in range(100):
    print(next(gen))
print("-------------------")

# Generator Methods
# send() Method
# The send() method allows you to send a value to the generator:

def echo_generator():
    while True:
        received = yield
        print('Received:', received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send('Hello')
gen.send('World')
print("-------------------")

# close() Method
# The close() method stops the generator:

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print('Generator closed')
gen = my_gen()
print(next(gen))
gen.close()
print("-------------------")

# Python range
